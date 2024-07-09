from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column, relationship
from sqlalchemy import String,Integer,ForeignKey,Float
from typing import List
class Base(DeclarativeBase):
    pass

db= SQLAlchemy(model_class = Base)

class Category(db.Model):
    __tablename__ ="category"
    id :Mapped[int] = mapped_column(primary_key =True)
    category_name :Mapped[str] = mapped_column(String(50))
    product : Mapped[List["Product"]] = relationship()


class Product(db.Model):
    __tablename__ = "products"
    product_id   : Mapped[int] = mapped_column(primary_key=True)
    product_name : Mapped[str] = mapped_column(String(50))
    price        : Mapped[int] = mapped_column(Integer)
    category_id  : Mapped[int] =mapped_column(ForeignKey("category.id"))
    category: Mapped["Category"] = relationship("Category", back_populates="product")
    image: Mapped["Image"] = relationship(back_populates="product")

    
class Image(db.Model):
    __tablename__= "image"
    image_id : Mapped[int] = mapped_column(primary_key=True)
    image : Mapped[str] = mapped_column(String(255))
    p_id : Mapped[int] =mapped_column(ForeignKey("products.product_id"))
    product : Mapped["Product"]= relationship("Product", back_populates="image")


def init_db(db_uri='postgresql://postgres:1234@localhost:5432/flaskdb'):
    logger = logging.getLogger("FlaskApp")
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    logger.info("Created database")

def get_session(db_uri):
    engine = create_engine(db_uri)
    Session = sessionmaker(bind = engine)
    session = Session()
    return session