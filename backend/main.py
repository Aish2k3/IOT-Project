from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import pymongo
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient("mongodb://localhost:27017")
# client = pymongo.MongoClient("mongodb://mongodb:27017")

db = client["IoTSensor"]

collection = db["MUP6050"]

test_value = {
    "sensorName": "testvalue",
    "userName": "testvalue",
    "accX": 2,
    "accY": 2,
    "accZ": 2,
    "rotX": 2,
    "rotY": 2,
    "rotZ": 2,
    "temp": 96.4
}

@app.route('/', methods=['GET'])
def hello():
    return "Up and Running"

@app.route('/sensorData', methods=['POST'])
def receive_sensor_data():
    required_fields = ["sensorName", "userName", "accX", "accY", "accZ", "rotX", "rotY", "rotZ", "temp"]

    try:
        data = request.get_json()

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        sensor_name = data["sensorName"]
        user_name = data["userName"]
        acc_x = data["accX"]
        acc_y = data["accY"]
        acc_z = data["accZ"]
        rot_x = data["rotX"]
        rot_y = data["rotY"]
        rot_z = data["rotZ"]
        temp = data["temp"]

        timestamp = datetime.now()

        inp_data = {
            "sensorName": sensor_name,
            "userName": user_name,
            "accX": acc_x,
            "accY": acc_y,
            "accZ": acc_z,
            "rotX": rot_x,
            "rotY": rot_y,
            "rotZ": rot_z,
            "temperature": temp,
            "timestamp": timestamp
        }

        inserted_data = collection.insert_one(inp_data)
        inserted_id = str(inserted_data.inserted_id)

        response_data = {
            "_id": inserted_id,
            "message": "Data Inserted"
        }

        return jsonify(response_data)

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/sensorData",methods=["GET"])
def getAll_sensor_data():
    try:
        userName = request.args.get("userName")
        users = collection.find({"userName": userName})

        if not userName:
            return jsonify(test_value), 200

        output = [{
            'sensorName': user['sensorName'],
            'accX': user['accX'],
            'accY': user['accY'],
            'accZ': user['accZ'],
            'rotX': user['rotX'],
            'rotY': user['rotY'],
            'rotZ': user['rotZ'],
            'temperature': user['temperature'],
            'timestamp': user['timestamp']
        } for user in users]

        return jsonify(output), 200

    except Exception as e:
        return jsonify({'error': str(e)}, 500)

@app.route("/sensorData", methods=["DELETE"])
def delete_sensor_data():
    try:
        userName = request.args.get("userName")

        if not userName:
            return jsonify({"error": "Missing 'userName' parameter"}), 200

        result = collection.delete_many({"userName": userName})

        return jsonify({
            "message": f"Deleted {result.deleted_count} records for userName: {userName}"
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}, 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
