from configur import app,db,jsonify,HTTPStatus,request,hashlib,os,jwt_required,get_jwt_identity,email_regex,allowedextensions,secure_filename,myId,uploadfolder
app.config['JWT_CSRF_CHECK_FORM'] = True

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowedextensions
    
@app.route("/update/user2",methods=['PATCH'])
@jwt_required(fresh=True)
def updateUser2():
    try: 
        current_user = get_jwt_identity()
        id = current_user['id']
        files = request.files.getlist('picture')
        address = request.form.get("address")
        city = request.form.get("city")
        email = request.form.get("email")
        gender = request.form.get("gender")
        name = request.form.get("name")
        password = request.form.get("password")
        phone_number = request.form.get("phone_number")

        #check_email = db.execute(f"select email from tbl_user where id_user = '{id}'")
        hashpassword = hashlib.md5((password+os.getenv("SALT_PASSWORD")).encode())
        if address == "" or city == "" or gender =="" or name =="" or password =="" or phone_number == "":
            response ={
                "Data": "Bad Request",
                "Message": "All Data Must be Filled"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        # elif check_email:
        #     updateUser = (f"update tbl_user set email ='' where id_user = '{id}' ")
        #     db.execute(updateUser)
        if email_regex.match(email):
            for i in files:
                if i and allowed_file(i.filename):
                    filename = secure_filename(i.filename)
                    picfilename = str(myId) + '_' + filename 
                    i.save(os.path.join(uploadfolder,picfilename))
                    success = True
                if success:
                    updateUser = (f"update tbl_user set email ='{email}' ,password = '{hashpassword.hexdigest()}',name='{name}',gender='{gender}',address='{address}',city='{city}',phone_number='{phone_number}',picture='{picfilename}' where id_user = '{id}'")
                    db.execute(updateUser)
                    response={
                                "Data": updateUser,
                                "Message": "Data Updated"
                            }
                    return jsonify(response),HTTPStatus.OK
            if not files:
                    updateUser = (f"update tbl_user set  email ='{email}',password = '{hashpassword.hexdigest()}',name='{name}',gender='{gender}',address='{address}',city='{city}',phone_number='{phone_number}' where id_user = '{id}'")
                    db.execute(updateUser)
                    response={
                                "Data": updateUser,
                                "Message": "Data Updated"
                            }
                    return jsonify(response),HTTPStatus.OK
        else:
            response={
                "Data": "Bad Request",
                "Message": "Email is not Valid"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
    except Exception as err:
        response ={
            "data": str(err),
            "message": "Bad Gateway"
        }
        return jsonify(response), HTTPStatus.BAD_GATEWAY

       
