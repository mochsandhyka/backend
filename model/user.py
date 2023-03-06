from .base import db,Required,PrimaryKey,Set,date,Optional,uuid

class User(db.Entity):
    _table_ = "tbl_user"
    id_user = PrimaryKey(uuid.UUID,default=uuid.uuid4)
    username = Required(str,unique = True)
    email = Required(str,unique = True)
    password = Required(str)
    name = Required(str)
    gender = Required(str)
    address = Required(str)
    city = Required(str)
    phone_number = Required(str)
    date_register = Required(date)
    picture = Optional(str)
    role = Required(str)
    borrowedbook = Set('BorrowedBook') 