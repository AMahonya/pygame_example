from datetime import datetime
from typing import Annotated
from app.config import settings, get_db_url

from sqlalchemy.orm import  sessionmaker, DeclarativeBase
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy import create_engine


DATABASE_URL = get_db_url()


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Base(DeclarativeBase):
    pass




















# DATABASE_URL = settings.DATABASE_URL
# if not DATABASE_URL:
#     raise ValueError("DATABASE_URL environment variable is not set.")
#
# try:
#     engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True) # add echo and pool_pre_ping for better debugging
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#     Base = declarative_base()
#
# except Exception as e:
#     print(f"Error connecting to the database: {e}")
#     raise
#
#
#     # Connect to an existing database
# conn = psycopg2.connect(host=settings.DB_HOST,
#                         dbname=settings.DB_NAME,
#                         user=settings.DB_USER,
#                         password=settings.DB_PASSWORD,
#                         cursor_factory=RealDictCursor)
#
# # Open a cursor to perform database operations
# cursor = conn.cursor()