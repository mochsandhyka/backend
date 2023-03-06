from configur import app,db,jsonify,HTTPStatus,request

@app.route("/update/book/category/<id>")
def listUpdateBookCategory(id):
    try:
        updateCategoryById = db.execute(f"select category from tbl_book_category where id_book_category = {id}")
        data = []
        for i in updateCategoryById:
            data.append({
                "category": i[0]
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
    

@app.route("/update/book/category/<id>",methods=['PUT'])
def updateBookCategory(id):
    try:
        bodyJson = request.json
        updateBookCategory = (f"update tbl_book_category set category='{bodyJson['category']}' where id_book_category = {id}")
        db.execute(updateBookCategory)
        response = {
            "data": updateBookCategory,
            "message": "Data updated"
        }
        return jsonify(response), HTTPStatus.ACCEPTED
    except Exception as err:
        response = {
            "data": str(err),
            "message": "Bad Gateway"
        }
        return jsonify(response), HTTPStatus.ACCEPTED
