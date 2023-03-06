from .base import db,Required,PrimaryKey,Set,Optional
from .user import User
from datetime import date

class BorrowedBook(db.Entity):
    _table_ = "tbl_borrowed_book"
    id_book_borrowed = PrimaryKey(int, auto = True)
    loan_date = Required(date)
    date_of_return = Optional(date)
    status = Required(bool)
    user = Required(User,column='id_user') 
    borrowed_detail = Set('BorrowedDetail')
