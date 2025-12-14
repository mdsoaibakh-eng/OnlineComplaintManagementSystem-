from app import create_app, db
from models import Category

app = create_app()

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()
    print("Creating all tables...")
    db.create_all()
    
    print("Seeding categories...")
    if not Category.query.first():
        default_categories = ['Academic', 'Infrastructure', 'Hostel', 'Canteen', 'Other']
        for name in default_categories:
            db.session.add(Category(name=name))
        db.session.commit()
    print("Database reset complete.")
