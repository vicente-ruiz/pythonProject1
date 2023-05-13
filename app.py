from flask import Flask, render_template, current_app
import requests
import uvicorn
import json

app = Flask(__name__)
# current_app = app


@app.route("/")
def index():
    return "Baba booey"


# Using 0.0.0.0 lets our app run on all available network interfaces, so we will get an ip for our localhost and machine
# app.run(host="0.0.0.0", port=80)
if __name__ == '__main__':
    # uvicorn.run(app, host="127.0.0.1", port=80) # Run on localhost
    app.run(host="0.0.0.0", port=80)

