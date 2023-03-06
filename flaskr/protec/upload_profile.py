from configur import app,request,get_jwt_identity,jwt_required,jsonify,HTTPStatus,secure_filename,os,uploadfolder,allowedextensions,maxcontent,db,url_for
app.config['JWT_CSRF_CHECK_FORM'] = True
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowedextensions

@app.route("/upload/profile",methods = ['PUT','GET'])
@jwt_required()
def upload():
    current_user = get_jwt_identity()
    a = {
            "id_user": current_user[0][0],
            "pic_user": current_user[0][1]
        }
    if request.method == 'GET':
        return current_user
    else:
        try:
            if 'picture' not in request.files:
                response ={
                        "Data": "Bad Request",
                        "Message": "No Picture Selected"
                    }
                return jsonify(response),HTTPStatus.BAD_REQUEST
            files = request.files.getlist('picture')
            success = False
            id = current_user[0][0]
            for user in db.select(f"select id_user,picture from tbl_user where id_user = '{id}'"): 
                user = {
                    "id_user": user[0],
                    "pic_user": user[1]
                }  
            for file in files:
                if file and allowed_file(file.filename):
                    try:
                        os.remove(os.path.join(uploadfolder, user['pic_user']))
                    except Exception:
                        pass
                    filename = secure_filename(file.filename)
                    picname = str(user['id_user']) + "_" + filename
                    file.save(os.path.join(uploadfolder, picname))
                    success = True
                else:
                    response ={
                        "Data": "Bad Request",
                        "Message": "File Type is Not Allowed"
                    }
                    return jsonify(response),HTTPStatus.BAD_REQUEST
            if success:
                uploadFoto = (f"update tbl_user set picture='{picname}' where id_user = '{id}'")
                db.execute(uploadFoto)
                resp = jsonify({'message' : 'Files successfully uploaded',
                                "data": picname})
                resp.status_code = 201
                return resp 
            else:
                response ={
                        "Data": "Bad Request",
                        "Message": "Bad"
                    }
                return jsonify(response),HTTPStatus.BAD_REQUEST
        
        except Exception as err:
            response ={
                        "Data": str(err),
                        "Message": "Bad Gateway"
                    }
            return jsonify(response),HTTPStatus.BAD_GATEWAY


