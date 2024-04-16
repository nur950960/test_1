from sqlalchemy import Column, Integer, String, Text

from settings import Base 


class Product(Base): 
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True) 
    title = Column(String, nullable=False)
    price = Column(Integer) 
    description = Column(Text) 
