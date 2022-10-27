from flask import Flask
app = Flask(__name__)
from flask_pymongo import PyMongo
app.config['MONGODB_NAME'] = 'citizens_database'
app.config["MONGO_URI"] = "mongodb://localhost:27017/citizens_database"
mongo = PyMongo(app)
if __name__ == '__main__':
    app.secret_key = 'my_secret'
    # app.run(debug=True)
    p = mongo.db.people.find({})
    for people in p:
        print(people['fio'] + '\n')