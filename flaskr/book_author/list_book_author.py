from configur import app,jsonify,HTTPStatus,db

@app.route('/list/book/author')
def listBookAuthor(): 
    try:
        listBookAuthor = db.select(f"select *from tbl_book_author")
        listSelectBookAuthor = []
        for i in listBookAuthor:
            dictBookCategory ={
                "id": i[0],
                "name": i[1],
                "email": i[2],
                "gender": i[3],
                "address": i[4],
                "phone_number": i[5]
            }
            listSelectBookAuthor.append(dictBookCategory)
        response = {
            "data": listSelectBookAuthor,
            "message":"Data"
        }
        return jsonify(response),HTTPStatus.OK
    except Exception as err:
        response = {
            "data": str(err),
            "message":"BAD GATEWAY"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY