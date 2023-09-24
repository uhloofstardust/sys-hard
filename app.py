# import signal
# import os
from flask import Flask, render_template
import subprocess as subp

app = Flask(__name__, template_folder="./public/")

# def handle_sigint(signum, frame):
#     print("Received SIGINT. Shutting down gracefully...")
# signal.signal(signal.SIGINT, handle_sigint)

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/hello")
def func():
    return "hello there"

# @app.route('/shutdown', methods=['POST'])
# def shutdown():
#     print("Shutting down Flask server...")
#     os._exit(0)
