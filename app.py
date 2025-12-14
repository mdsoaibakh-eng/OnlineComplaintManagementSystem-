import os
from flask import Flask, render_template, redirect, url_for, flash, request, session
from dotenv import load_dotenv
from models import db, Admin, User, Category, Complaint, StatusLog
from markupsafe import Markup, escape
from datetime import datetime
from werkzeug.utils import secure_filename

load_dotenv()

# ===========================
# Login Decorators
# ===========================
def admin_login_required(f):
    from functools import wraps
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("admin_id"):
            flash("Please log in as admin.", "error")
            return redirect(url_for("admin_login"))
        # Verify admin exists in DB
        admin = Admin.query.get(session["admin_id"])
        if not admin:
            session.pop("admin_id", None)
            flash("Session invalid. Please login again.", "error")
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)
    return wrapper

def user_login_required(f):
    from functools import wraps
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("user_id"):
            flash("Please log in to access this page.", "error")
            return redirect(url_for("user_login"))
        # Verify user exists in DB
        user = User.query.get(session["user_id"])
        if not user:
            session.pop("user_id", None)
            session.pop("user_name", None)
            flash("Session invalid. Please login again.", "error")
            return redirect(url_for("user_login"))
        return f(*args, **kwargs)
    return wrapper

# ===========================
# Create App
# ===========================
def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-secret')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    db.init_app(app)

    # Create tables and seed categories
    with app.app_context():
        db.create_all()
        if not Category.query.first():
            default_categories = ['Academic', 'Infrastructure', 'Hostel', 'Canteen', 'Other']
            for name in default_categories:
                db.session.add(Category(name=name))
            db.session.commit()

    @app.template_filter('nl2br')
    def nl2br_filter(s):
        if s is None:
            return ""
        return Markup("<br>".join(escape(s).splitlines()))

    # ===========================
    # PUBLIC ROUTES
    # ===========================
    @app.route("/")
    def index():
        return render_template("index.html")

    # ===========================
    # ADMIN AUTH & DASHBOARD
    # ===========================
    @app.route("/admin/login", methods=["GET", "POST"])
    def admin_login():
        if request.method == "POST":
            username = request.form.get("username").strip()
            password = request.form.get("password").strip()
            admin = Admin.query.filter_by(username=username).first()
            if not admin or not admin.check_password(password):
                flash("Invalid credentials.", "error")
                return render_template("admin_login.html")
            session["admin_id"] = admin.id
            flash("Welcome Admin.", "success")
            return redirect(url_for("admin_dashboard"))
        return render_template("admin_login.html")

    @app.route("/admin/register", methods=["GET", "POST"])
    def admin_register():
        # Ideally this should be protected or removed in production
        if request.method == "POST":
            username = request.form.get("username").strip()
            password = request.form.get("password").strip()
            if Admin.query.filter_by(username=username).first():
                flash("Username taken.", "error")
                return render_template("admin_register.html")
            admin = Admin(username=username)
            admin.set_password(password)
            db.session.add(admin)
            db.session.commit()
            flash("Admin registered.", "success")
            return redirect(url_for("admin_login"))
        return render_template("admin_register.html")

    @app.route("/admin/logout")
    def admin_logout():
        session.pop("admin_id", None)
        flash("Logged out.", "info")
        return redirect(url_for("index"))

    @app.route("/admin/dashboard")
    @admin_login_required
    def admin_dashboard():
        status_filter = request.args.get('status')
        if status_filter:
            complaints = Complaint.query.filter_by(status=status_filter).order_by(Complaint.created_at.desc()).all()
        else:
            complaints = Complaint.query.order_by(Complaint.created_at.desc()).all()
        return render_template("admin_dashboard.html", complaints=complaints)

    @app.route("/admin/reports")
    @admin_login_required
    def admin_reports():
        total = Complaint.query.count()
        pending = Complaint.query.filter_by(status='Pending').count()
        in_progress = Complaint.query.filter_by(status='In-progress').count()
        resolved = Complaint.query.filter_by(status='Resolved').count()
        rejected = Complaint.query.filter_by(status='Rejected').count()
        
        # Simple category stats
        categories = Category.query.all()
        cat_stats = []
        for cat in categories:
            count = Complaint.query.filter_by(category_id=cat.id).count()
            cat_stats.append({'name': cat.name, 'count': count})
            
        return render_template("admin_reports.html", 
                               total=total, 
                               pending=pending, 
                               in_progress=in_progress, 
                               resolved=resolved, 
                               rejected=rejected,
                               cat_stats=cat_stats)

    @app.route("/admin/complaint/<int:complaint_id>", methods=["GET", "POST"])
    @admin_login_required
    def admin_complaint_detail(complaint_id):
        complaint = Complaint.query.get_or_404(complaint_id)
        if request.method == "POST":
            new_status = request.form.get("status")
            assigned_to = request.form.get("assigned_to")
            comments = request.form.get("comments")
            
            changes = []
            if new_status and new_status != complaint.status:
                log = StatusLog(
                    complaint_id=complaint.id,
                    old_status=complaint.status,
                    new_status=new_status,
                    comments=f"Status changed. {comments}"
                )
                complaint.status = new_status
                db.session.add(log)
                changes.append("Status updated")

            if assigned_to and assigned_to != complaint.assigned_to:
                complaint.assigned_to = assigned_to
                # Log assignment change
                log = StatusLog(
                    complaint_id=complaint.id,
                    old_status=complaint.status,
                    new_status=complaint.status,
                    comments=f"Assigned to: {assigned_to}. {comments}" if not changes else f"Assigned to {assigned_to}"
                )
                db.session.add(log)
                changes.append("Assignment updated")
            
            if not changes and comments:
                 # Just a comment
                log = StatusLog(
                    complaint_id=complaint.id,
                    old_status=complaint.status,
                    new_status=complaint.status,
                    comments=comments
                )
                db.session.add(log)
                changes.append("Comment added")

            if changes:
                db.session.commit()
                flash("Complaint updated successfully.", "success")
            else:
                flash("No changes made.", "info")

            return redirect(url_for("admin_complaint_detail", complaint_id=complaint.id))
        
        return render_template("admin_complaint_detail.html", complaint=complaint)

    # ===========================
    # USER AUTH & COMPLAINTS
    # ===========================
    @app.route("/user/register", methods=["GET", "POST"])
    def user_register():
        if request.method == "POST":
            name = request.form.get("name").strip()
            email = request.form.get("email").strip()
            password = request.form.get("password").strip()
            
            if User.query.filter_by(email=email).first():
                flash("Email already registered.", "error")
                return render_template("user_register.html")
            
            user = User(name=name, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash("Registration successful. Please login.", "success")
            return redirect(url_for("user_login"))
        return render_template("user_register.html")

    @app.route("/user/login", methods=["GET", "POST"])
    def user_login():
        if request.method == "POST":
            email = request.form.get("email").strip()
            password = request.form.get("password").strip()
            user = User.query.filter_by(email=email).first()
            
            if not user or not user.check_password(password):
                flash("Invalid email or password.", "error")
                return render_template("user_login.html")
            
            session["user_id"] = user.id
            session["user_name"] = user.name
            flash("Logged in successfully.", "success")
            return redirect(url_for("user_dashboard"))
        return render_template("user_login.html")

    @app.route("/user/logout")
    def user_logout():
        session.pop("user_id", None)
        session.pop("user_name", None)
        flash("Logged out.", "info")
        return redirect(url_for("index"))

    @app.route("/user/profile", methods=["GET", "POST"])
    @user_login_required
    def user_profile():
        user = User.query.get(session["user_id"])
        if request.method == "POST":
            name = request.form.get("name").strip()
            email = request.form.get("email").strip()
            password = request.form.get("password").strip()

            if not name or not email:
                flash("Name and Email are required.", "error")
                return redirect(url_for("user_profile"))

            user.name = name
            # Check if email is taken by another user
            existing_user = User.query.filter_by(email=email).first()
            if existing_user and existing_user.id != user.id:
                flash("Email already in use.", "error")
                return redirect(url_for("user_profile"))
            
            user.email = email
            if password:
                user.set_password(password)
            
            db.session.commit()
            session["user_name"] = user.name
            flash("Profile updated successfully.", "success")
            return redirect(url_for("user_profile"))
        
        return render_template("user_profile.html", user=user)

    @app.route("/user/dashboard")
    @user_login_required
    def user_dashboard():
        user = User.query.get(session["user_id"])
        complaints = Complaint.query.filter_by(user_id=user.id).order_by(Complaint.created_at.desc()).all()
        return render_template("user_dashboard.html", user=user, complaints=complaints)

    @app.route("/complaint/new", methods=["GET", "POST"])
    @user_login_required
    def file_complaint():
        if request.method == "POST":
            category_id = request.form.get("category")
            title = request.form.get("title")
            description = request.form.get("description")
            file = request.files.get("attachment")
            
            filename = None
            if file and file.filename:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            if not title or not description:
                flash("Please fill in all fields.", "error")
                return redirect(url_for("file_complaint"))
                
            complaint = Complaint(
                user_id=session["user_id"],
                category_id=category_id,
                title=title,
                description=description,
                attachment=filename
            )
            db.session.add(complaint)
            db.session.commit()
            
            # Initial log
            log = StatusLog(
                complaint_id=complaint.id,
                old_status=None,
                new_status="Pending",
                comments="Complaint filed."
            )
            db.session.add(log)
            db.session.commit()
            
            flash("Complaint filed successfully.", "success")
            return redirect(url_for("user_dashboard"))
            
        categories = Category.query.all()
        return render_template("file_complaint.html", categories=categories)

    @app.route("/complaint/<int:complaint_id>")
    @user_login_required
    def complaint_detail(complaint_id):
        complaint = Complaint.query.get_or_404(complaint_id)
        if complaint.user_id != session["user_id"]:
            flash("Unauthorized access.", "error")
            return redirect(url_for("user_dashboard"))
        return render_template("complaint_detail.html", complaint=complaint)

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
