from .base import db,PrimaryKey,Required,Optional,Set,uuid

class BookAuthor(db.Entity):
    _table_ = "tbl_book_author"
    id_book_author = PrimaryKey(uuid.UUID,default=uuid.uuid4)
    name = Required(str, unique=True)
    email = Optional(str)
    gender = Optional(str)
    address = Optional(str)
    phone_number = Optional(str)
    book = Set('Book')