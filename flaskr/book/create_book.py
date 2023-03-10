from configur import app,request,generateId,db,jsonify,HTTPStatus,allowed_file,secure_filename,os,uploadfolder
from model.book import Book


@app.route("/create/book",methods=['POST'])
def createBook():
    try:
        myId = generateId()
        files = request.files.getlist('picture')
        stock = request.form.get('stock')
        book_title = request.form.get('book_title')
        book_category = request.form.get('book_category')
        book_author = request.form.get('book_author')
        book_publisher = request.form.get('book_publisher')

        checkbook = db.select(f"select * from tbl_book where book_title = '{book_title}' and id_book_author = '{book_author}' ")
        if stock == "" or book_title == "" or book_category == "" or book_author == "" or book_publisher == "":
            response ={
                "Data": "Bad Request",
                "Message": "All Data Must be Filled"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        elif checkbook:
            response = {
                "Data": "Bad Request",
                "Message": "Book Already Registered"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        else:
            for i in files:
                if i and allowed_file(i.filename):
                    filename = secure_filename(i.filename)
                    picfilename = str(myId) + '_' + filename
                    i.save(os.path.join(uploadfolder,picfilename))
                    success = True
                if success:
                    createBook = (f"insert into tbl_book(id_book,stock,book_title,id_book_category,id_book_author,id_book_publisher,picture) values('{myId}','{stock}','{book_title}','{book_category}','{book_author}','{book_publisher}','{picfilename}')")
                    db.execute(createBook)
                    response = {
                        "Data": "Success",
                        "Message": "Data Created"
                    }
                    return jsonify(response),HTTPStatus.OK
                elif picfilename == "":
                    response = {
                        "Data": "Bad Request",
                        "Message": "Picture Must be Upload"
                    }
                    return jsonify(response),HTTPStatus.BAD_REQUEST
    except Exception as err:
        response ={
            "data": str(err),
            "message": "Bad Gateway"
        }
        return jsonify(response), HTTPStatus.BAD_GATEWAY

    
