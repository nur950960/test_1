from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base, sessionmaker 
from decouple import config 

# db_url = 'driver://db_user:password@db_host/db_name'
db_url = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}/{config('DB_NAME')}"

engine = create_engine(db_url)

# создаем базовый класс для всех таблиц 
Base = declarative_base()

# создаем класс для сессий (один обьект - одна сессия)
SessionLocal = sessionmaker(bind=engine)