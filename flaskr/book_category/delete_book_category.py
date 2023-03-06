from configur import app,jsonify,HTTPStatus,db

@app.route("/delete/book/category/<id>",methods=['DELETE'])
def deleteBookCategory(id):
    try:
        selectById = (f"select id_book_category,category from tbl_book_category where id_book_category = {id}")
        dictData={}
        for i in db.execute(selectById):
            dictData = {
                "id_book_category": i[0],
                "category": i[1]
            } 
        if not dictData:
            response = {
                "data": "Bad Request",
                "message": "Data Not Found"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
        elif dictData:
            deleteById = (f"delete from tbl_book_category where id_book_category = {id}")
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
