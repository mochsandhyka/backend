from configur import app,db,jsonify,HTTPStatus,request


@app.route("/update/book/publisher/<id>")
def listUpdateBookPublisher(id):
    try:
        updatePublisherById = db.execute(f"select id_book_publisher,name,email,address,phone_number from tbl_book_publisher where id_book_publisher = {id}")
        data = []
        for i in updatePublisherById:
            data.append({
                "id_book_publisher": i[0],
                "name": i[1],
                "email": i[2],
                "address": i[3],
                "phone_number": i[4],
                
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
    

@app.route("/update/book/publisher/<id>",methods=['PUT'])
def updateBookPublisher(id):
    try:
        bodyJson = request.json
        updateBookPublisher = (f"update tbl_book_publisher set name='{bodyJson['name']}', email='{bodyJson['email']}',address='{bodyJson['address']}',phone_number='{bodyJson['phone_number']}' where id_book_publisher = {id}")
        db.execute(updateBookPublisher)
        response = {
            "data": updateBookPublisher,
            "message": "Data updated"
        }
        return jsonify(response), HTTPStatus.OK
    except Exception as err:
        response = {
            "data": str(err),
            "message": "Bad Gateway"
        }
        return jsonify(response), HTTPStatus.BAD_GATEWAY
