from configur import app,db,jsonify,HTTPStatus,request,hashlib,os,jwt_required,get_jwt_identity

@app.route("/update/user")
@jwt_required()
def listUpdateUser(id):
    try:
        current_user = get_jwt_identity
        id = current_user[0][0]
        updateUserById = db.execute(f"select username,email,password,gender,address,phone_number,city,picture from tbl_user where id_user = {id}")
        data = []
        for i in updateUserById:
            data.append({
                "username": i[0],
                "email": i[1],
                "password": i[2],
                "name": i[3],
                "gender": i[4],
                "address": i[5],
                "phone_number": i[6],
                "city": i[7],
                "picture": i[8]
            })
        if not data:
            respon = {
                "data": "Bad Request",
                "message": "No Data Found"
            }
            return jsonify(respon), HTTPStatus.BAD_REQUEST
        respon = {
            "data": data[0],
            "message": "Data is Found"
        }
        return jsonify(respon),HTTPStatus.OK
    except Exception as err:
        respon = {
            "data": str(err),
            "message": "bad gateway"
        }
        return jsonify(respon),HTTPStatus.BAD_GATEWAY
    

@app.route("/update/user",methods=['PUT'])
@jwt_required()
def updateUser(id):
    try:
        current_user = get_jwt_identity
        id = current_user[0][0]
        bodyJson = request.json
        hashpass = hashlib.md5((bodyJson['password']+os.getenv("SALT_PASSWORD")).encode())
        updateUser = (f"update tbl_user set username='{bodyJson['username']}' ,password = '{hashpass.hexdigest()}',email='{bodyJson['email']}',name='{bodyJson['name']}',gender='{bodyJson['gender']}' where id_user = {id}")
        db.execute(updateUser)
        response = {
            "data": updateUser,
            "message": "Data updated"
        }
        return jsonify(response), HTTPStatus.ACCEPTED
    except Exception as err:
        response = {
            "data": str(err),
            "message": "Bad Gateway"
        }
        return jsonify(response), HTTPStatus.ACCEPTED
