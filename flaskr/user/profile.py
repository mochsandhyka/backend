from configur import app,jwt_required,get_jwt_identity,jsonify,HTTPStatus,db

@app.route("/profile")
@jwt_required()
def list():
    try:
        current_user = get_jwt_identity() 
        if current_user:
            id = current_user[0][0] 
            for i in db.select(f"select id_user,username,email,name,gender,address,city,phone_number,picture from tbl_user where id_user = '{id}'"):
                Data = {
                    "id": i[0],
                    "username": i[1],
                    "email": i[2], 
                    "name": i[3], 
                    "gender": i[4],
                    "address": i[5],
                    "city": i[6],
                    "phone_number": i[7],
                    "picture": i[8]
                } 
            response = {
                    "data": Data,
                    "message": "Success"
                }
            return jsonify(response),HTTPStatus.OK
        else:
            response = {
                    "data": "Bad Request",
                    "message": "You Are Not Logged In"
                }
    except Exception:
        pass