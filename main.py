from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.arhive_model import Base, Arhive

# SQLite database connection
engine = create_engine("sqlite:///E:/Microl/new_data/Roshod_gasy_new/2025-01-09.sqlite")  # Replace with your database path

# Create tables if they don't exist (optional)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query all rows
records = session.query(Arhive).all()
for record in records:
    print(record)
