from configur import app,request,jsonify,HTTPStatus,email_regex,hashlib,db,os,allowedextensions,maxcontent,db,url_for,secure_filename,os,uploadfolder

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowedextensions

@app.route("/auth/reg/user", methods = ['POST'])
def regUser():
    try:
        files = request.files.getlist('picture')
        jsonBody = request.json
        errors = {}
        success = False
        checkUser = db.select(f"select * from tbl_user where username = '{jsonBody['username']}' or email = '{jsonBody['email']}'")
        if jsonBody['city'] == "" or jsonBody['username'] == "" or jsonBody['email'] == "" or jsonBody['password'] == "" or jsonBody['name'] == "" or jsonBody['gender'] == "" or jsonBody['address'] == "" or jsonBody['phone_number'] == "" or jsonBody['role'] == "":
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
        elif email_regex.match(jsonBody['email']):
            for i in files:
                if i and allowed_file(i.filename):
                    filename = secure_filename(i.filename)
                    picfilename = jsonBody['username'] + filename 
                    i.save(os.path.join(uploadfolder,picfilename))
                    success = True
                if success:
                    hashpassword = hashlib.md5((jsonBody['password']+ os.getenv("SALT_PASSWORD")).encode())
                    createUser = (f"insert into tbl_user(username,email,password,name,gender,address,city,phone_number,date_register,picture,role) values('{jsonBody['username']}','{jsonBody['email']}','{hashpassword.hexdigest()}','{jsonBody['name']}','{jsonBody['gender']}','{jsonBody['address']}','{jsonBody['city']}','{jsonBody['phone_number']}',now(),{filename},'{jsonBody['role']}')")
                    db.execute(createUser)
                    response={
                                "Data": jsonBody,
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