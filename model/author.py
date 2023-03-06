from .base import db,PrimaryKey,Required,Optional,Set

class BookAuthor(db.Entity):
    _table_ = "tbl_book_author"
    id_book_author = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    email = Optional(str)
    gender = Optional(str)
    address = Optional(str)
    phone_number = Optional(str)
    book = Set('Book')