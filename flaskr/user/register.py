from configur import app,request,jsonify,HTTPStatus,email_regex,hashlib,db,os,myId

@app.route("/auth/register/user", methods = ['POST'])
def registerUser():
    try:
        jsonBody = request.json
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
            hashpassword = hashlib.md5((jsonBody['password']+ os.getenv("SALT_PASSWORD")).encode())
            createUser = (f"insert into tbl_user(id_user,username,email,password,name,gender,address,city,phone_number,date_register,picture,role) values('{myId}','{jsonBody['username']}','{jsonBody['email']}','{hashpassword.hexdigest()}','{jsonBody['name']}','{jsonBody['gender']}','{jsonBody['address']}','{jsonBody['city']}','{jsonBody['phone_number']}',now(),'a.jpg','{jsonBody['role']}')")
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