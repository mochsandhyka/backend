from configur import app,db,jsonify,HTTPStatus,secure_filename,url_for,allowedextensions,get_jwt_identity,jwt_required
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowedextensions

@app.route("/list/user")
#@jwt_required()
def listUser():
   # try:
  #      current_user = get_jwt_identity()
   #     role = current_user[0][1]
    #    if role == 'admin':
            listUser = db.select(f"select id_user,username,email,name,gender,address,city,phone_number,picture,password from tbl_user where role = 'user'")
            y = []
            for i in listUser:
                y.append(i)
            listSelectUser = []
            for i in y:
                dictUser ={
                    "id": i[0],
                    "username": i[1],
                    "email": i[2], 
                    "name": i[3], 
                    "gender": i[4],
                    "address": i[5],
                    "city": i[6],
                    "phone_number": i[7],
                    "picture": i[8],
                    "password": i[9]
                }
                listSelectUser.append(dictUser)
            response = {
                    "data": listSelectUser,
                    "message": "Success"
                }
            return jsonify(response),HTTPStatus.OK
    #     else:
    #         response = {
    #                 "data": "Bad Request",
    #                 "message": "You are not allowed here"
    #             }
    #         return jsonify(response),HTTPStatus.BAD_REQUEST
    # except Exception as err:
    #     response = {
    #         "data": str(err),
    #         "message": "Bad Gateway"
    #     }
    #     return jsonify(response),HTTPStatus.BAD_GATEWAY