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



# route to load a drone with medication items
@app.route('/add-load/<id>', methods=['PUT'])
def load_drone(id):
    _id = id
    _json =request.json

    all = upper + lower + str(num) + symbal
    all_upper = upper + str(num) + symbal
    temp = random.sample(all,length)
    temp_upper = random.sample(all_upper,length)

    _medName = "".join(temp)
    _medWeight = _json['medWeight']
    _medCode = "".join(temp_upper)
    _medImage = _json['medImage']


    if mongo.db.drone.find_one({ '$and': [{'_id': ObjectId(_id)},{'weightLimit': {'$gt':_medWeight}},{'loadState': {'$eq':"IDLE"}}]}):
        if _medName and _medWeight and _medCode and _medImage and request.method == 'PUT':

            _loadState = 'LOADING'

            mongo.db.drone.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'loadState':_loadState, 'medName':_medName,'medWeight':_medWeight,'medImage':_medImage,'medCode':_medCode}})

            res =jsonify("updated")
            res.status_code = 200
            return res
        else:
            return not_added()

    else:
        message ={
            'status': 404,
            'message':'Drone not available or Weight too heavy ' + request.url
        }        

        res = jsonify(message)
        res.status_code = 404
        return res




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
