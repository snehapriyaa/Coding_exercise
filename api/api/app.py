#Imports
from flask import Flask, request, Response, jsonify
import json

#Creates flask object
app = Flask(__name__)

#API Endpoint for inserting new user and number.
@app.route('/',methods=['POST'])
def add_user():
  request_data = request.get_json()
  #If request is null, user is informed to provide valid details
  if(request_data is None or (request_data is not None and (request_data.get("name") is None or request_data.get("phone") is None))):
     response = Response(json.dumps(jsonify({"status":400,"message":"Enter valid user details."}).json), 400, mimetype='application/json')
     return response
  #If request is valid, the new user is added successfully to the json file.
  else:
     save_data(jsonify({request_data["name"]:request_data["phone"]}).json)
     message = "Added user "+request_data["name"]+" with phone number " + str(request_data["phone"])+""
     response = Response(json.dumps(jsonify({"status":200,"message":message}).json),200 , mimetype='application/json')
     return response

#API Endpoint for retrieving a user number.
@app.route('/name/<name>',methods=['GET'])
def get_number(name):
    json_data =  load_data()
    #If user name is null or not found in the json record, user is informed to provide valid name.
    if(json_data.get(name) is None):
     response = Response(json.dumps(jsonify({"status":400,"message":"Enter valid user name."}).json), 400, mimetype='application/json')
     return response
    else:
    #If request is valid, the user number is successfully retrieved.
        message = "Found user "+name+" with phone number " + str(json_data[name])+""
        response = Response(json.dumps(jsonify({"status":200,"message":message}).json), 200, mimetype='application/json')
        return response

#API Endpoint for updating a user number.
@app.route('/',methods=['PUT'])
def update_number():
    data = request.get_json()
    json_data =  load_data()
     #If request is null or user not found in the json record, user is informed to provide valid name.
    if(data=={} or data.get("name") is None):
       response = Response(json.dumps(jsonify({"status":400,"message":"Enter valid user details to update."}).json), 400, mimetype='application/json')
       return response
    else:
    #If request is valid, the user number is successfully updated.
       update_one_item_in_json(data["name"], data["phone"], json_data)
       message = "Updated user "+data["name"]+" with phone number " + str(data["phone"])+""
       response = Response(json.dumps(jsonify({"status":200,"message":message}).json), 200, mimetype='application/json')
       return response

#API Endpoint for deleting a user record.
@app.route('/name/<name>',methods=['DELETE'])
def delete_record(name):
    json_data =  load_data()
    #If request is null or user not found in the json record, user is informed to provide valid name.
    if(json_data.get(name) is None):
       response = Response(json.dumps(jsonify({"status":400,"message":"User not found. Enter valid user details."}).json), 400, mimetype='application/json')
       return response
    else:
    #If request is valid, the user number is successfully deleted.
       delete_one_item_from_json(name,json_data)
       message = "Successfully deleted user "+name+""
       response = Response(json.dumps(jsonify({"status":200,"message":message}).json), 200, mimetype='application/json')
       return response

# Load the File
def load_data():
    with open(r"api/Users.json") as f:
        return json.load(f)

# Save the file with new data
def save_data(json_data):
    with open(r"api/Users.json", 'w') as f:
        json.dump(json_data, f, indent=4)

# Delete One Item from Json
def delete_one_item_from_json(name,json_data):
	del json_data[name]
	save_data(json_data)

# Update One Item from JSON
def update_one_item_in_json(name, data, json_data):
	json_data[name] = data
	save_data(json_data)
