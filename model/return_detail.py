from .base import db,Required,PrimaryKey,Set,Optional
from .return_book import ReturnBook
from .book import Book

class ReturnDetail(db.Entity):
    _table_ = "tbl_detail_return_book"
    return_book = Required(ReturnBook, column='id_book_return')
    book = Required(Book, column='id_book')