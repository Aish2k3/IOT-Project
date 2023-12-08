from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import pymongo
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
CORS(app)

# client = pymongo.MongoClient("mongodb://localhost:27017")
client = pymongo.MongoClient("mongodb://mongodb:27017")

db = client["IoTSensor"]

collection = db["MUP6050"]

@app.route('/', methods=['GET'])
def hello():
    return "Up and Running"


@app.route('/sensorData', methods=['POST'])
def receive_sensor_data():
    
    data = request.get_json()
    
    sensor_name = data.get("sensorName")
    user_name = data.get("userName")
    acc_x = data.get("accX")
    acc_y = data.get("accY")
    acc_z = data.get("accZ")
    
    rot_x = data.get("rotX")
    rot_y = data.get("rotY")
    rot_z = data.get("rotZ")
    
    temp = data.get("temp")
    
    timestamp = datetime.now()

    inp_data = {
        "sensorName":sensor_name,
        "userName":user_name,
        "accX":acc_x,
        "accY":acc_y,
        "accZ":acc_z,
        "rotX":rot_x,
        "rotY":rot_y,
        "rotZ":rot_z,
        "temperature":temp,
        "timestamp":timestamp
    }

    inserted_data = collection.insert_one(inp_data)
    inserted_id = str(inserted_data.inserted_id)

    response_data = {
        "_id": inserted_id,
        "message": "Data Inserted"
    }

    return jsonify(response_data)

@app.route("/sensorData",methods=["GET"])
def getAll_sensor_data():
    try:
        userName = request.args.get("userName")
        users = collection.find({"userName":userName})
        
        output = [{
            'sensorName': user['sensorName'],
            'accX':user['accX'],
            'accY':user['accY'],
            'accZ':user['accZ'],
            'rotX':user['rotX'],
            'rotY':user['rotY'],
            'rotZ':user['rotZ'],
            'temperature':user['temperature'],
            'timestamp':user['timestamp']
        } for user in users]
        
        
        return jsonify(output), 200
    except Exception as e:
        return jsonify({'error': str(e)}, 500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
