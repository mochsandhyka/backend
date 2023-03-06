from configur import app,email_regex,request,jsonify,HTTPStatus,db

@app.route('/create/book/author', methods=['POST'])
def createBookAuthor():
    try:
        jsonBody = request.json
        checkBookAuthor = db.select(f"select * from tbl_book_author where name = '{jsonBody['name']}'")
        if jsonBody['name'] == "" or jsonBody['email'] == "" or jsonBody['gender'] == "" or jsonBody['address'] == "" or jsonBody['phone_number'] == ""  :
            response ={
                "Data": "Bad Request",
                "Message": "All Data Must be Filled"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif checkBookAuthor:
            response ={
                "Data": "Bad Request",
                "Message": "Author Already Registered"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif not checkBookAuthor and email_regex.match(jsonBody['email']) :
            createBookAuthor = (f"insert into tbl_book_author(name,email,gender,address,phone_number) values('{jsonBody['name']}','{jsonBody['email']}','{jsonBody['gender']}','{jsonBody['address']}','{jsonBody['phone_number']}')")
            db.execute(createBookAuthor)
            response={
                "Data": jsonBody,
                "Message": "Data Created"
            }
            return jsonify(response),HTTPStatus.OK
        elif not email_regex.match(jsonBody['email']):
            response={
                "Data": "BAD REQUEST",
                "Message": "EMAIL NOT VALID"
            }
            return jsonify(response),HTTPStatus.OK
    except Exception as err:
        response ={
            "data": str(err),
            "message": "Bad Gateway"
        }
        return jsonify(response), HTTPStatus.BAD_GATEWAY