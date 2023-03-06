from configur import app,db,jsonify,HTTPStatus,request

 
@app.route("/update/book/author/<id>")
def listUpdateBookAuthor(id):
    try:
        updateAuthorById = db.execute(f"select id_book_author,name,email,gender,address,phone_number from tbl_book_author where id_book_author = {id}")
        data = []
        for i in updateAuthorById:
            data.append({
                "id_book_publisher": i[0],
                "name": i[1],
                "email": i[2],
                "gender": i[3],
                "address": i[4],
                "phone_number": i[5],
                
            })
        if not data:
            respon = {
                "data": "Bad Request",
                "message": "No Data Found"
            }
            return jsonify(respon), HTTPStatus.BAD_REQUEST
        respon = {
            "data": data[0],
            "message": "data is found"
        }
        return jsonify(respon),HTTPStatus.OK
    except Exception as err:
        respon = {
            "data": str(err),
            "message": "bad gateway"
        }
        return jsonify(respon),HTTPStatus.BAD_GATEWAY
    

@app.route("/update/book/author/<id>",methods=['PUT'])
def updateBookAuthor(id):
    try:
        bodyJson = request.json
        updateBookAuthor = (f"update tbl_book_author set name='{bodyJson['name']}', email='{bodyJson['email']}',gender='{bodyJson['gender']}',address='{bodyJson['address']}',phone_number='{bodyJson['phone_number']}' where id_book_author = {id}")
        db.execute(updateBookAuthor)
        response = {
            "data": updateBookAuthor,
            "message": "Data updated"
        }
        return jsonify(response), HTTPStatus.OK
    except Exception as err:
        response = {
            "data": str(err),
            "message": "Bad Gateway"
        }
        return jsonify(response), HTTPStatus.BAD_GATEWAY
