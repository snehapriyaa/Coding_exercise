CRUD-Web API-with-Python-and-Flask

Requirements
Python3
Flask pip install flask
Introducing API
Application Programming Interface (API) allows information to be manipulated by other programs via the internet.

API Terminology
HTTP(Hypertext Transfer Protocol) : is the primary means of communicating data on the web. 
URL(Uniform Resource Locator) : An address for a resource on the web. A URL consists of a protocol(http://), domain , and optional path (/about). A URL describes the location of a specific resource, such as a web page.
JSON(JavaScript Object Notation) is a text-based data storage format that is designed to be easy to read for both humans and machines. JSON is generally the most common format for returning data through an API, XML being the second most common.
REST(REpresentational State Transfer) is a philosophy that describes some best practices for implementing APIs. APIs designed with some or all of these principles in mind are called REST APIs.
Flask
Flask web framework is used to write an API. Flask maps HTTP requests to Python functions.

Installation:
1)Go to api folder.
2)Setting up virtual environment:
On Linux:
virtualenv -p python3 Test
source Test/bin/activate
pip install flask

Path to JSON file:
Path to JSON file is configured as "api/Users.json" in the code.
Users.json file is expected to be in api/api/Users.json as per the submitted folder structure.

On Windows:
py -m venv Test
.\Test\Scripts\activate
pip install flask

Run the flask application with the command python py __main__.py
 We see output similar to below:
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
This message means that Flask is running the application locally(on your computer) at that address.Follow the above link, http://127.0.0.1:5000/ using your web browser to see the running application

What Flask does:
Flask maps HTTP requests to Python functions. In our case, we've mapped one URL path('/') to one function home.
When we connect to Flask server at http://127.0.0.0:5000/, Flask checks if there is a match between the path provided and a defined function.
The process of mapping URLs to functions is called routing.
@app.route('/', methods=['GET'])
The methods list (methods=['GET']) is a keyword argument that lets Flask known what kind of HTTP requests are allowed.

app = Flask(__name__) - Creates the Flask application object, which contains data about the application and also methods(object functions) that tell the application to do certain actions.

Creating the API

Let's add some data(entries on user name and number) as a list of dictionaries. Each dictionary will contain name, phone for each user.
$ curl -X POST http://localhost -H 'Content-Type: application/json' -d '{"name": "john", "phone": 9876543210}'
{"status":201,"message":"Success: Added user john with phone number 9876543210"} is the expected response.

Run the code (navigate to api folder in the command line and enter python __main__.py. Once the server is running, visit the route URL to view the data in the catalog for GET request:
http://127.0.0.1:5000/name/john
Flask has a jsonify function that converts lists and dictionaries to JSON format.
Here we dealt with the GET requests which corresponds to reading from a JSON file.
$ curl -X GET http://localhost/?name=john
{"status":200,"message":"Found user john with phone number 9876543210"}

This API pulls in data from a json file implements error handling and filters users by name.

The methods list (methods=['PUT']) updates the user value and 'DELETE' deletes the value.
$ curl -X PUT http://localhost -H 'Content-Type: application/json' -d '{"name": "john", "phone": 7651234980}'
{"status":201,"message":"Success: Updated user john with phone number 7651234980"}

$ curl -X DELETE http://localhost/?name=john
{"status":200,"message":"Successfully deleted user john"}
The prevailing design philosophy of modern APIs is called REST. The  REST is based on the four methods defined by the HTTP protocol : POST, GET, PUT and DELETE.

