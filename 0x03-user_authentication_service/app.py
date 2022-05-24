#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify, request, abort, make_response, json, redirect
from auth import Auth

AUTH = Auth()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def idex():
    """JSON form"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """users"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": "{}".format(user.email),
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """sessions"""
    email = request.form.get['email']
    password = request.form.get['password']

    if AUTH.valid_login(email, password) is False:
        abort(401)
    session_id = AUTH.create_session(email)
    resp = make_response({"email": email, "message": "logged in"})
    resp.set_cookie('session_id', session_id)
    return resp


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """logout"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
