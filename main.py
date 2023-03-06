from configur import app,regex,email_regex,jwt,ponyapp,os,re,hashlib,db

#from configur import app

# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = os.getenv("JWT_ACCESS_TOKEN_EXPIRES")

import flaskr.user.register as register
import flaskr.user.login as login
import flaskr.user.list_admin as list_admin
import flaskr.user.list_user as list_user
import flaskr.user.delete_user as delete_user
import flaskr.user.update_user as update_user
import flaskr.user.reg as reg

import flaskr.book_category.create_book_category as create_book_category
import flaskr.book_category.list_book_category as list_book_category
import flaskr.book_category.update_book_category as update_book_category
import flaskr.book_category.delete_book_category as delete_book_category

import flaskr.book_author.create_book_author as create_book_author
import flaskr.book_author.list_book_author as list_book_author
import flaskr.book_author.update_book_author as update_book_author
import flaskr.book_author.delete_book_author as delete_book_author

import flaskr.book_publisher.create_book_publisher as create_book_publisher
import flaskr.book_publisher.list_book_publisher as list_book_publisher
import flaskr.book_publisher.update_book_publisher as update_book_publisher
import flaskr.book_publisher.delete_book_publisher as delete_book_publisher

import flaskr.protec.upload_profile
import flaskr.protec.profile
import flaskr.protec.protec