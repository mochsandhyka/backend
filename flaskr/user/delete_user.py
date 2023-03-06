from configur import app,db,jsonify,HTTPStatus

@app.route("/delete/user/<id>",methods=['DELETE'])
def deleteUser(id):
    try:
        selectById = (f"select id_user,role from tbl_user where id_user = {id}")
        dictData={}
        for i in db.execute(selectById):
            dictData = {
                "id": i[0],
                "role": i[1]
            } 
        if not dictData:
            response = {
                "data": "Bad Request",
                "message": "Data Not Found"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
        elif dictData['role'] == 'user' :
            deleteById = (f"delete from tbl_user where id_user = {id}")
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
