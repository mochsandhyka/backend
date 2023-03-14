from configur import app,select,db,uuid,get_jwt_identity,jwt_required,generateId,jsonify,HTTPStatus

@app.route("/cc")
@jwt_required()
def listBooked():
    currentuser = get_jwt_identity()
    id = currentuser['id']
    top = 3
    select = db.execute(f"select b.loan_date,c.book_title from tbl_detail_borrowed_book as a left join tbl_borrowed_book as b on (a.id_book_borrowed = b.id_book_borrowed) left join tbl_book as c on (a.id_book = c.id_book) where b.id_user = '{id}' and b.status = False")
    listbuku = []
    for i in select:
        dict ={
            "loan_date": i[0],
            "book_title": i[1]
        }
        listbuku.append(dict)
    return listbuku

@app.route("/cc2")
@jwt_required()
def listBooked2():
    currentuser = get_jwt_identity()
    id = currentuser['id']
    top = 3
    select = db.execute(f"select b.loan_date,c.book_title from tbl_detail_borrowed_book as a left join tbl_borrowed_book as b on (a.id_book_borrowed = b.id_book_borrowed) left join tbl_book as c on (a.id_book = c.id_book) where b.id_user = '{id}' and b.status = True limit {top} ")
    listbuku = []
    for i in select:
        dict ={
            "loan_date": i[0],
            "book_title": i[1]
        }
        listbuku.append(dict)
    return listbuku


@app.route("/bb")
@jwt_required()
def listBook():
    currentUser = get_jwt_identity()
    id = currentUser['id']
    # selectbuku = db.execute(f"select a.id_book,a.stock,a.book_title,b.category,c.name,d.name from tbl_book as a left join tbl_book_category as b on (a.id_book_category = b.id_book_category) left join tbl_book_author as c on (a.id_book_author = c.id_book_author) left join tbl_book_publisher as d on (a.id_book_publisher = d.id_book_publisher)")

    selecta = db.execute(f"select id_book,book_title,stock from tbl_book where id_book not in(select a.id_book from tbl_detail_borrowed_book as a left join tbl_borrowed_book as b on (a.id_book_borrowed = b.id_book_borrowed) where id_user = '{id}') or id_book in (select a.id_book from tbl_detail_return_book as a left join tbl_return_book as b on (a.id_book_return = b.id_book_return) where id_user = '{id}') and stock > 0")
    listbuku = []
    for i in selecta:
         dict = {
            "id_book":i[0],
            "book_title":i[1],
            "stock": i[2]
         }
         listbuku.append(dict)

    return jsonify(listbuku)

@app.route("/bb/<book>",methods = ['POST'])
@jwt_required()
def borrowBook(book):
    try:
        currentUser = get_jwt_identity()
        id = currentUser['id'] 
        myId = generateId()
        f = False

        a = db.select(f"select id_user from tbl_borrowed_book where id_user = '{id}'")
        x = []
        for i in a:
             x.append(i)
        if len(x) >= 3:
            response={
                  "Data":"Bad Request",
                  "Message": "You Already borrow 3 Book"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        
        else:
            db.execute(f"insert into tbl_borrowed_book(id_book_borrowed,loan_date,date_of_return,status,id_user) values ('{myId}',NOW(),NOW() + INTERVAL '7 DAYS',{f},'{id}')")
            db.execute(f"insert into tbl_detail_borrowed_book(id_book_borrowed,id_book) values('{myId}','{book}')")
            response={
                  "Data":"Success",
                  "Message": "Please Wait Admin to Acc"
            }
            return jsonify(response),HTTPStatus.OK
    except Exception as err:
        return str(err)
        
@app.route("/acc")
@jwt_required()
def listAccBook():
    try:
        currentUser = get_jwt_identity()
        role = currentUser['role']
        if role == 'admin':
            acc = db.execute(f"select * from tbl_borrowed_book where status = False")
            l = []
            for i in acc:
                dict = {
                    "id": i[0],
                    "loan date": i[1],
                    "date return": i[2],
                    "status": i[3],
                    "id user": i[4]
                }
                l.append(dict)

            return l
        else:
            return "You Are not allowed here"
    except Exception as err:
        return str(err)

@app.route("/acc/<id>",methods = ['PATCH'])
@jwt_required()
def accBook(id):
    try:
        currentUser = get_jwt_identity()
        role = currentUser['role']
        if role == 'admin':
            acc = (f"update tbl_borrowed_book set status = True where id_book_borrowed = '{id}'")
            # db.execute(f"update tbl_detail_borrowed_book a join tbl_book b on a.id_book = b.id_book set b.stock = (b.stock - 1) where a.id_book_borrowed = '{id}' ")
            upd = (f"update tbl_book tbl1 set stock = (stock - 1) from tbl_detail_borrowed_book tbl2 where tbl1.id_book = tbl2.id_book and id_book_borrowed = '{id}'")
            db.execute(acc)
            db.execute(upd)
            return "d",HTTPStatus.OK
        else:
            return "You Are Non Allowed Here",HTTPStatus.BAD_REQUEST
    except Exception as err:
        response = str(err)
        return response,HTTPStatus.BAD_GATEWAY

















        # db.execute(f"insert into tbl_borrowed_book(id_book_borrowed,loan_date,date_of_return,status,id_user) values ('{myId}',NOW(),NOW() + INTERVAL '7 DAYS',{f},'{id}')")
        # db.execute(f"insert into tbl_detail_borrowed_book(id_book_borrowed,id_book) values('{myId}','{book}')")
       
       
    
    # bookselectbyid = db.execute(f"select a.loan_date, a.date_of_return,b.name,c.name,d.judul_buku, extract(day from a.date_of_return) - extract(day from now()) from borrowing as a left join admin as b on(a.fk_admin = b.pk_admin) left join public.user as c on(a.fk_user = c.pk_user) left join book as d on(a.fk_book = d.pk_buku) where fk_book = {id}")
    # countBook = select(f"select id_borrowed_book from tbl")
        
    # except Exception as err:
    #     return "b"

#klik pinjam --> ambil id_book insert tbl detail
#insert peminjaman -> id_book_borrowed, loan_date, date_of_return, status,user,borrowed_detail


