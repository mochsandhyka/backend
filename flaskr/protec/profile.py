from configur import app,jwt_required,get_jwt_identity,jsonify,HTTPStatus,db

@app.route("/profile")
@jwt_required()
def list():
    try:
        current_user = get_jwt_identity() 
        if current_user:
            _id = current_user[0][0]
            a = {}
            for i in db.select(f"select id_user,name,username,email,gender,picture from tbl_user where id_user = '{_id}'"):
                a = {
                    "id": i[0],
                    "name": i[1],
                    "username": i[2], 
                    "email": i[3], 
                    "gender": i[4],
                    "picture": i[5]
                } 
            response = {
                    "data": a,
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