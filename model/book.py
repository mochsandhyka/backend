from .base import db,Required,PrimaryKey,Set,Optional,uuid
from .book_category import BookCategory
from .author import BookAuthor
from .publisher import Publisher

class Book(db.Entity):
    _table_ = "tbl_book"
    id_book = PrimaryKey(uuid.UUID,default=uuid.uuid4)
    stock = Required(int)
    book_title = Required(str)
    book_category = Required(BookCategory,column='id_book_category')
    book_author = Required(BookAuthor,column='id_book_author')
    book_publisher = Required(Publisher,column='id_book_publisher')
    borrowed_detail = Set('BorrowedDetail')
    return_detail = Set('ReturnDetail')
    picture = Optional(str)