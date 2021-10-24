"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()


Pet.query.delete()

# Add sample employees and departments
p1 = Pet(name="Sunny", species="Dog", age=1, notes="3 months old")


db.session.add(p1)
db.session.commit()

