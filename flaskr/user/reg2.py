from configur import myId,app,request,jsonify,HTTPStatus,email_regex,hashlib,db,os,allowedextensions,maxcontent,db,url_for,secure_filename,os,uploadfolder

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowedextensions

@app.route("/auth/reg/user2", methods = ['POST'])
def regUser2():
    try:
        files = request.files.getlist('picture')
        address = request.form.get("address")
        city = request.form.get("city")
        email = request.form.get("email")
        gender = request.form.get("gender")
        name = request.form.get("name")
        password = request.form.get("password")
        phone_number = request.form.get("phone_number")
        role = request.form.get("role")
        username = request.form.get("username") 
        json = request.form.to_dict('json')
        print(json)
        success = False
        checkUser = db.select(f"select * from tbl_user where username = '{username}' or email = '{email}'")
        if address == "" or city == "" or email == "" or gender =="" or name =="" or password =="" or phone_number == "" or role =="" or username == "":
            response ={
                "Data": "Bad Request",
                "Message": "All Data Must be Filled"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif checkUser:
            response ={
                "Data": "Bad Request",
                "Message": "Username or Email already registered"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif email_regex.match(email):
            for i in files:
                if i and allowed_file(i.filename):
                    filename = secure_filename(i.filename)
                    picfilename = username + filename 
                    i.save(os.path.join(uploadfolder,picfilename))
                    success = True
                if success:
                    hashpassword = hashlib.md5((password+ os.getenv("SALT_PASSWORD")).encode())
                    createUser = (f"insert into tbl_user(id_user,username,email,password,name,gender,address,city,phone_number,date_register,picture,role) values('{myId}','{username}','{email}','{hashpassword.hexdigest()}','{name}','{gender}','{address}','{city}','{phone_number}',now(),'{filename}','{role}')")
                    db.execute(createUser)
                    response={
                                "Data": "data",
                                "Message": "Data Created"
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