from .base import db, Required,PrimaryKey,Set,uuid

class BookCategory(db.Entity):
    _table_ = "tbl_book_category"
    id_book_category = PrimaryKey(uuid.UUID,default=uuid.uuid4)
    category = Required(str, unique=True)
    book = Set('Book')