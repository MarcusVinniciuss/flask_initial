from flask_sqlalchemy import model
from sqlalchemy.orm import load_only
from ma import ma 
from models.book import BookModel

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        load_instance = True