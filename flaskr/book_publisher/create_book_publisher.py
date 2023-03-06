from configur import app,request,jsonify,HTTPStatus,email_regex,db

@app.route('/create/book/publisher', methods=['POST'])
def createBookPublisher():
    try:
        jsonBody = request.json
        checkBookPublisher = db.select(f"select * from tbl_book_publisher where name = '{jsonBody['name']}'")
        if jsonBody['name'] == "" or jsonBody['email'] == "" or jsonBody['address'] == "" or jsonBody['phone_number'] == ""  :
            response ={
                "Data": "Bad Request",
                "Message": "All Data Must be Filled"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif checkBookPublisher:
            response ={
                "Data": "Bad Request",
                "Message": "Publisher Already Registered"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif not checkBookPublisher and email_regex.match(jsonBody['email']) :
            createBookPublisher = (f"insert into tbl_book_publisher(name,email,address,phone_number) values('{jsonBody['name']}','{jsonBody['email']}','{jsonBody['address']}','{jsonBody['phone_number']}')")
            db.execute(createBookPublisher)
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