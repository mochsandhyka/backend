from configur import app,jwt_required,get_jwt_identity,jsonify,HTTPStatus,db

# USER ACCESS BOOK
@app.route("/list/book")
@jwt_required()
def accessBook():
    current_user = get_jwt_identity
    _id = current_user['id_user']
    _role = current_user['role']
    if _role == "user":
        historyBook = db.select(f"select  ")

# GET IDENTITY
    
@app.route("/pro")
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    _id = current_user['id_user']
    _role = current_user['role']
    print(_id)
    if _role == "user":
        listSelectUser = [] 
        for i in db.select(f"select id_user,name,username,email,gender,picture from tbl_user where id_user = '{_id}'"):
            listSelectUser.append({
                "id": i[0],
                "name": i[1],
                "username": i[2], 
                "email": i[3], 
                "gender": i[4],
                "picture": i[5]
            })
        response = {
            "data": "BAD REQUEST",
            "message": "YOU ARE NOT ALLOWED HERE"
        }
        return jsonify(response), HTTPStatus.BAD_REQUEST
    elif _role == "admin":
        response = {
            "data": current_user,
            "message": "ok"
        }
        return jsonify(response), HTTPStatus.OK
    else:
        response = {
            "data": "BAD REQUEST",
            "message": "BAD REQUEST"
        }
        return jsonify(response),HTTPStatus.BAD_REQUEST
    