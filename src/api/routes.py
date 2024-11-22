"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
@api.route('/signup', methods=['POST'])
def signup():
    request_body=request.json 
    email=request_body.get("email")
    password=request_body.get("password")
    user_exists=User.query.filter_by(email=email).first()
    if user_exists:
        return jsonify(error="Email already exists"), 400
    newuser=User(email=email, password=password, is_active=True)
    db.session.add(newuser)
    db.session.commit()
    return jsonify(message= "signup successful")

@api.route('/login', methods=['POST'])
def login():
    request_body=request.json 
    email=request_body.get("email")
    password=request_body.get("password")

    user_exists=User.query.filter_by(email=email, password=password).first()

    if not user_exists:
        return jsonify(error="Invalid credentials"), 400
    
    token=create_access_token(identity=user_exists.email)

    return jsonify(message= "login successful", token=token)

@api.route('/private', methods=['GET'])
@jwt_required()
def get_access():
    return jsonify(message="authentication successful")