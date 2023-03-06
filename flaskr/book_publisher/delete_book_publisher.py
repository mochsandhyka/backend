from configur import app,db,jsonify,HTTPStatus

@app.route("/delete/book/publisher/<id>",methods=['DELETE'])
def deleteBookPublisher(id):
    try:
        selectById = (f"select id_book_publisher from tbl_book_publisher where id_book_publisher = {id}")
        dictData={}
        for i in db.execute(selectById):
            dictData = {
                "id_book_publisher": i[0]
            } 
        if not dictData:
            response = {
                "data": "Bad Request",
                "message": "Data Not Found"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
        elif dictData:
            deleteById = (f"delete from tbl_book_publisher where id_book_publisher = {id}")
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
