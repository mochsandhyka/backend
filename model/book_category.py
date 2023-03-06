from .base import db, Required,PrimaryKey,Set

class BookCategory(db.Entity):
    _table_ = "tbl_book_category"
    id_book_category = PrimaryKey(int, auto=True)
    category = Required(str, unique=True)
    book = Set('Book')