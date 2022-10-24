# This is a sample Python script.
from flask import Flask, render_template
from config import Configuration
from time import time, asctime
from flask_admin import Admin
import pymongo
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config.from_object(Configuration)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["citizens_database"]
import sys
admin = Admin(app)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
