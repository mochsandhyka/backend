
from configur import app,request,jsonify,HTTPStatus,db

@app.route('/create/book/category', methods=['POST'])
def createBookCategory():
    try:
        jsonBody = request.json
        checkBookCategory = db.select(f"select * from tbl_book_category where category = '{jsonBody['category']}'")
        if jsonBody['category'] == "":
            response ={
                "Data": "Bad Request",
                "Message": "All Data Must be Filled"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif checkBookCategory:
            response ={
                "Data": "Bad Request",
                "Message": "Category Already Registered"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif not checkBookCategory:
            createBookCategory = (f"insert into tbl_book_category(category) values('{jsonBody['category']}')")
            db.execute(createBookCategory)
            response={
                "Data": jsonBody,
                "Message": "Data Created"
            }
            return jsonify(response),HTTPStatus.OK
    except Exception as err:
        response ={
            "data": str(err),
            "message": "Bad Gateway"
        }
        return jsonify(response), HTTPStatus.BAD_GATEWAY