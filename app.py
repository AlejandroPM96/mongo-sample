#Hello tesing pushes
from flask import Flask
from flask import request
from pymongo import MongoClient 
import json
from bson import ObjectId

import os


app = Flask(__name__)
mongo_client = MongoClient(os.environ['MONGO_URI']) 
db = mongo_client["EPAMTEST"]
collection = db["random"]

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@app.route("/health")
def getHealth():
    """
    The endpoint for checking health of app
    """
    return "ok"

@app.route("/getAll")
def getPalindrome():
    """
    The endpoint for retrieve all docs

    **Example request**
        .. sourcecode:: http

            GET /palindrome?word=anilina
            HOST: example.com
            ACCEPT: application/json

    Example Response:
    {
        "name": "anilina",
        "palindrome": true,
        "sorted": {
            "a": 2,
            "i": 2,
            "l": 1,
            "n": 2
        },
        "length": 7
    }
    """
    x = collection.find()
    result = JSONEncoder().encode(list(x))
    return {"response": json.loads(result)}

@app.route("/insert", methods=["POST"])
def insert(): 
    doc = request.get_json()
    rec_id1 = collection.insert_one(doc)
    return {"inserted": rec_id1.acknowledged}


if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    port = os.environ['HOME'] if os.environ.get('HOME',"") != "" else 8080
    if type(port) is str:
        app.run(host='0.0.0.0', port=8080, debug=True)
    else:
        app.run(host='0.0.0.0', port=port, debug=True)
