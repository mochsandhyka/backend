import db_settings 
from .base import db
from . import author, book, book_category, borrowed_book, borrowed_detail, publisher


db.bind(**db_settings.db_params)
db.generate_mapping(create_tables=True)