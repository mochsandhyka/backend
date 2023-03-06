from flask import Flask,request,jsonify,url_for
import os,re,hashlib,uuid
from pony.flask import Pony
from flask_jwt_extended import get_csrf_token,get_jwt,set_refresh_cookies,create_refresh_token,jwt_manager,JWTManager,set_access_cookies,create_access_token,jwt_required,get_jwt_identity,unset_access_cookies
from http import HTTPStatus
from model import db
from werkzeug.utils import secure_filename
from flask_cors import CORS


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]")
myId = uuid.uuid4()
#app.config['JWT_ACCESS_TOKEN_EXPIRES'] = os.getenv('ACCESS_TOKEN_EXPIRES')
#jwtexp = app.config['JWT_ACCESS_TOKEN_EXPIRES'] 

app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER")
app.config['MAX_CONTENT_LENGHT'] = os.getenv("MAX_CONTENT_LENGHT")
app.config['ALLOWED_EXTENSIONS'] = os.getenv("ALLOWED_EXTENSION")
uploadfolder = app.config['UPLOAD_FOLDER']
allowedextensions = app.config['ALLOWED_EXTENSIONS']
maxcontent = app.config['MAX_CONTENT_LENGHT']
 
jwt = JWTManager(app)
ponyapp = Pony(app)
CORS(app)
 


