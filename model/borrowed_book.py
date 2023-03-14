from .base import db,Required,PrimaryKey,Set,Optional,uuid,date
from .user import User 

class BorrowedBook(db.Entity):
    _table_ = "tbl_borrowed_book"
    id_book_borrowed = PrimaryKey(uuid.UUID,default=uuid.uuid4)
    loan_date = Required(date)
    date_of_return = Optional(date)
    status = Required(bool)
    user = Required(User,column='id_user')
    borrowed_detail = Set('BorrowedDetail')
    return_book = Set('ReturnBook')
