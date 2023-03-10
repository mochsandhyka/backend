from configur import app,select,db,uuid,get_jwt_identity,jwt_required,generateId,jsonify,HTTPStatus

@app.route("/bb/<book>",methods = ['POST'])
@jwt_required()
def borrowBook(book):
    # try:
        currentUser = get_jwt_identity()
        id = currentUser['id'] 
        myId = generateId()
        f = False

        a = db.select(f"select id_user from tbl_borrowed_book where id_user = '{id}'")
        x = []
        for i in a:
             x.append(i)
        if len(x) > 2:
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

@app.route("/acc",methods = ['PATCH'])
@jwt_required()
def accBook():
    # try:
        currentUser = get_jwt_identity()
        id = currentUser['id'] 
        t = True
        bookId = db.select(f"select id_book from tbl_book")
        a = []
        for i in bookId:
            a.append(i)
        book = a[0]

        # db.execute(f"insert into tbl_borrowed_book(id_book_borrowed,loan_date,date_of_return,status,id_user) values ('{myId}',NOW(),NOW() + INTERVAL '7 DAYS',{f},'{id}')")
        # db.execute(f"insert into tbl_detail_borrowed_book(id_book_borrowed,id_book) values('{myId}','{book}')")
       
        return "a"
    
    # bookselectbyid = db.execute(f"select a.loan_date, a.date_of_return,b.name,c.name,d.judul_buku, extract(day from a.date_of_return) - extract(day from now()) from borrowing as a left join admin as b on(a.fk_admin = b.pk_admin) left join public.user as c on(a.fk_user = c.pk_user) left join book as d on(a.fk_book = d.pk_buku) where fk_book = {id}")
    # countBook = select(f"select id_borrowed_book from tbl")
        
    # except Exception as err:
    #     return "b"

#klik pinjam --> ambil id_book insert tbl detail
#insert peminjaman -> id_book_borrowed, loan_date, date_of_return, status,user,borrowed_detail


