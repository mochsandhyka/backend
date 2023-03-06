from .base import db,Required,PrimaryKey,Set,Optional

class Publisher(db.Entity):
    _table_ = "tbl_book_publisher"
    id_book_publisher = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    email = Optional(str)
    address = Optional(str)
    phone_number = Optional(str)
    book = Set('Book')