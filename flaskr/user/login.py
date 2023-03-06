from configur import get_csrf_token,app,request,hashlib,jwt_required,set_refresh_cookies,create_refresh_token,get_jwt_identity,get_jwt,db,create_access_token,jsonify,HTTPStatus,unset_access_cookies,os,set_access_cookies
from datetime import timedelta,timezone,datetime
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=1)
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
 
# @app.after_request 
# def refresh_expiring_jwts(response):
#     try:
#         exp_timestamp = get_jwt()["exp"]
#         now = datetime.now(timezone.utc)
#         target_timestamp = datetime.timestamp(now + timedelta(minutes=0.1))
#         if target_timestamp > exp_timestamp:
#             refresh_token = create_refresh_token(identity=get_jwt_identity())
#             set_refresh_cookies(response, refresh_token)
#         return response
#     except (RuntimeError, KeyError):
#         # Case where there is not a valid JWT. Just return the original response
#         return response

# @app.route("/refresh", methods=["POST"])
# @jwt_required(refresh=True)
# def refresh():
#     try:
#         identity = get_jwt_identity()
#         access_token = create_access_token(identity=identity, fresh=False)
#         return jsonify(access_token=access_token)
#     except Exception as err:
#         response = {
#             "Data":"badgateway"
#         }
#         return jsonify(response),HTTPStatus.BAD_GATEWAY

@app.route("/auth/login/user", methods = ['POST'])
def loginUser():
    try:
        jsonBody = request.json
        hashpassword = hashlib.md5((jsonBody['password']+os.getenv("SALT_PASSWORD")).encode())
        user = db.select(f"select id_user,role from tbl_user where username = '{jsonBody['username']}' and password = '{hashpassword.hexdigest()}' ")
        if user:
            access_token = create_access_token(identity=user,fresh=True) 
            response = jsonify({
                "Data": get_csrf_token(access_token),
                "Message": "Login Success"
            })
            set_access_cookies(response, access_token)
            return response,HTTPStatus.OK
        else:
            response ={
                "Data": "Bad Request",
                "Message": "Username / Password is invalid"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
    except Exception as err:
        response ={
            "Data": str(err),
            "Message": "Bad Gateway"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY
    
@app.route("/auth/user/logout",methods=['POST']) 
def logout():
    try:
        response = jsonify("Logout Successfull")
        unset_access_cookies(response)
        return response,HTTPStatus.OK
    except Exception as err:
        return response,HTTPStatus.BAD_GATEWAY
    

    
