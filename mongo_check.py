#20,55  31/07
# from app import mydb
# print(mydb.name)
from flask import Flask, session
from time import asctime
import pymongo
app = Flask(__name__)
from flask_pymongo import PyMongo
app.config['MONGO_DBNAME'] = 'citizens_database'
app.config["MONGO_URI"] = "mongodb://localhost:27017/citizens_database"
mongo = PyMongo(app)
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["citizens_database"]
@app.route('/')
def home_page():
    if 'name' in session:
        pass
    online_users = mongo.db.people.find()
    cit = []
    text_to_send = ''
    row_num = 1
    # mongo.
    for x in online_users:
        pers = f"ФИО: {x['fio']} , дата рождения: {x['birth']}"
        cit.append(pers)
    return str(cit) + asctime() + 'Hop-Hop' + str(session.values())


if __name__ == '__main__':
    app.secret_key = 'my_secret'
    app.run(debug=True, port=8000)