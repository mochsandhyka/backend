from configur import get_csrf_token,app,request,hashlib,jwt_required,set_refresh_cookies,create_refresh_token,get_jwt_identity,get_jwt,db,create_access_token,jsonify,HTTPStatus,unset_access_cookies,os,set_access_cookies
from datetime import timedelta,timezone,datetime

 
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
        for i in user:
            userauth = {
                'id':i[0],
                'role': i[1]
            }
        if user:
            access_token = create_access_token(identity=userauth,fresh=True) 
            csrf_token = get_csrf_token(access_token)
            response = jsonify({
                "Data": csrf_token,
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
@jwt_required()
def logout():
    try:
        gji = get_jwt_identity()
        if gji:
            response = jsonify({
                "Data": "Success",
                "Message": "Logout Successfull"
            })
            unset_access_cookies(response)
            return response,HTTPStatus.OK
        else:
            response = jsonify({
                "Data": "Success",
                "Message": "Logout Successfull"
            })
            return response,HTTPStatus.BAD_REQUEST
    except Exception as err:
        response = jsonify({
                "Data": str(err),
                "Message": "Already Logout"
            })
        return response,HTTPStatus.BAD_GATEWAY
    

    
