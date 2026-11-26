
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL, text
from database.base import Base
from sqlalchemy.orm import sessionmaker
import models

# Load environment variables
load_dotenv()

# Build database URL safely
database_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", "5432")),
    database=os.getenv("DB_NAME")
)

# Create database engine
engine = create_engine(database_url, pool_pre_ping=True)

# Test database connection
def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version()"))
        print("Database connected successfully!")
        print(result.scalar())


# Run connection test and create tables
if __name__ == "__main__":
    test_connection()
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully!")

# Create database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Database dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()