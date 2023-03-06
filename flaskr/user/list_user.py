from configur import app,db,jsonify,HTTPStatus,secure_filename,url_for,allowedextensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowedextensions

@app.route("/list/user")
def listUser():
    listUser = db.execute(f"select id_user,name,username,email,gender,picture from tbl_user where role = 'user'")
    y = []
    for i in listUser:
        y.append(i)
    listSelectUser = []
    # filename = secure_filename(file.filename)
    # file_url = url_for('get_file',filename=filename)
    for i in y:
        dictUser ={
            "id": i[0],
            "name": i[1],
            "username": i[2], 
            "email": i[3], 
            "gender": i[4],
            "picture": i[5]
        }
        listSelectUser.append(dictUser)
    response = {
            "data": listSelectUser,
            "message": "Success"
        }
    return jsonify(response),HTTPStatus.OK