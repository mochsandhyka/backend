from configur import app,db,generateId

@app.route("/return")
def listReturnBook():
    selectpeminjaman = db.execute(f"select id_book_borrowed,loan_date,date_of_return,id_user from tbl_borrowed_book where id_book_borrowed not in(select id_book_borrowed from tbl_return_book)")
    listpeminjaman = []
    for i in selectpeminjaman:
        dictpeminjaman = {
            "id_book_borrowed": i[0],
            "loan_date": i[1],
            "date_of_return": i[2],
            "id_user": i[3]
        }
        listpeminjaman.append(dictpeminjaman)
    return listpeminjaman

@app.route("/return/<id>",methods=['POST'])
def returnBook(id):
    myId = generateId()
    select = db.execute(f"select extract(day from date_of_return)-extract(day from now()),a.id_user,a.id_book_borrowed,b.id_book from tbl_borrowed_book as a left join tbl_detail_borrowed_book as b on(a.id_book_borrowed = b.id_book_borrowed) where a.id_book_borrowed = '{id}' ")
    for i in select:
        dict = {
            "date_of_return": i[0],
            "id_user": i[1],
            "id_book_borrowed": i[2],
            "id_book": i[3]
        }

    
    iduser = dict['id_user']
    idbook = dict['id_book']
    idbookborrowed = dict['id_book_borrowed']
    dor = dict['date_of_return']
    if dor > 0:
        dor = 0
    else:
        dor = dor
    late_charge = dor * 1000 
    
    db.execute(f"insert into tbl_return_book (id_book_return,return_date,late_charge,id_user,id_book_borrowed) values ('{myId}',NOW(),{late_charge},'{iduser}','{idbookborrowed}')")
    db.execute(f"insert into tbl_detail_return_book(id_book_return,id_book) values ('{myId}','{idbook}')")
    db.execute(f"update tbl_book set stock = (stock + 1) where id_book = '{idbook}'")
    
    return "success"