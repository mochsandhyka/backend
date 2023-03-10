from .base import db,Required,PrimaryKey,Set,Optional,uuid

class Publisher(db.Entity):
    _table_ = "tbl_book_publisher"
    id_book_publisher = PrimaryKey(uuid.UUID,default=uuid.uuid4)
    name = Required(str, unique=True)
    email = Optional(str)
    address = Optional(str)
    phone_number = Optional(str)
    book = Set('Book')