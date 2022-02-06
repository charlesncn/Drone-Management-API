from crypt import methods
import string
from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify, request
import time


from bson.json_util import dumps
from bson.objectid import ObjectId

import random


#global variavbles
#generate random data
length = random.randint(10,100)
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = random.randint(0,9)
symbal = random.choice(['-', '_'])



app = Flask(__name__)


app.config['MONGO_URI'] = "mongodb://localhost:27017/drone" #connection string to the database



if __name__ == "__main__":
    app.run(debug=True)
