from .base import db,Required,PrimaryKey,Set,Optional,uuid,date
from .user import User
from .borrowed_book import BorrowedBook

class ReturnBook(db.Entity):
    _table_ = "tbl_return_book"
    id_book_return = PrimaryKey(uuid.UUID,default=uuid.uuid4)
    return_date = Required(date)
    late_charge = Optional(int)
    user = Required(User,column='id_user')
    borrowed = Required(BorrowedBook,column='id_book_borrowed')
    return_detail = Set('ReturnDetail')


