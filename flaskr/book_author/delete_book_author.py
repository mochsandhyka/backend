from configur import app,db,jsonify,HTTPStatus

@app.route("/delete/book/author/<id>",methods=['DELETE'])
def deleteBookAuthor(id):
    try:
        selectById = (f"select id_book_author from tbl_book_author where id_book_author = {id}")
        dictData={}
        for i in db.execute(selectById):
            dictData = {
                "id_book_author": i[0]
            } 
        if not dictData:
            response = {
                "data": "Bad Request",
                "message": "Data Not Found"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
        elif dictData:
            deleteById = (f"delete from tbl_book_author where id_book_author = {id}")
            db.execute(deleteById) 
            response = {
                "data": "Success",
                "message": "Delete Success"
            } 
            return jsonify(response), HTTPStatus.OK
        else:
            response = {
                "data": "Bad Request",
                "message": "Delete invalid"
            } 
            return jsonify(response), HTTPStatus.BAD_REQUEST
    except Exception as err:
        response={
            "data": str(err),
            "message": "bad gateway"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY
