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
mongo = PyMongo(app)


# route for registering a drone
@app.route('/add', methods=['POST'])
def add_drone():
    _json = request.json


    _serialNum = random.randint(10,100) #generate random serial number    
    _batteryCap = random.randint(0,100)  # Randomly select drone's battery capacity
    _weightLimit = random.choice([100,150,200,250,300,350,400,450,500]) # randomly choose weight limit of a drone
    _model = random.choice(['Lightweight', 'Middleweight', 'Cruiserweight', 'Heavyweight'])
    
    states = ['IDLE', 'LOADING', 'LOADED', 'DELIVERING', 'DELIVERED','RETURNING']# Randomly select drone state
    _loadState = random.choice(states)
    if _serialNum and _weightLimit and _batteryCap and _model and request.method == 'POST':

        #if battery is less than 25% don't assign LOANDING state
        if _batteryCap < 25:
            states.remove('LOADING')
            _loadState = random.choice(states)
            id = mongo.db.drone.insert_one({'serialNum':_serialNum, 'model':_model,'weightLimit':_weightLimit,'batteryCap':_batteryCap,'loadState':_loadState})

        

        else:
            id = mongo.db.drone.insert_one({'serialNum':_serialNum, 'model':_model,'weightLimit':_weightLimit,'batteryCap':_batteryCap,'loadState':_loadState})

        res = jsonify("Drone Added to the Fleet")
        res.status_code = 200
        return res

    else:
        return not_added()


@app.errorhandler(404)
def not_added(error=None):
    message ={
        'status': 404,
        'message':'DRONE NOT ADDED. MAKE SURE YOU ENTERED ALL PARAMS CORRECTLY' + request.url
    }        

    res = jsonify(message)

    res.status_code = 404

    return res



if __name__ == "__main__":
    app.run(debug=True)
