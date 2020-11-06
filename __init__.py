import os

import urllib3
from flask_cors import CORS

from component import mymysql

urllib3.disable_warnings()
from flask import Flask, make_response
import logging
from logging.handlers import TimedRotatingFileHandler
from exception import MyServiceException
import config
import route

config.init()

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = os.urandom(24)
CORS(app, supports_credentials=True)


@app.route('/<path:path>')
def static_path(path):
    return app.send_static_file(path)


@app.route('/')
def index():
    return app.send_static_file("index.html")


route.init(app)


@app.errorhandler(500)
def error(e):
    e = e.original_exception
    if isinstance(e, MyServiceException):
        print("e.msg: ", e.msg)
        custom_res = make_response(e.msg)
        custom_res.status = "500"
        return custom_res
    return e


mymysql.init(config.app_conf["mysql"])

if not os.path.exists("logs"):
    os.mkdir("logs")
if not os.path.exists("temp"):
    os.mkdir("temp")
formatter = logging.Formatter("[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
handler = TimedRotatingFileHandler("logs/flask.log", when="D", interval=1, backupCount=15, encoding="UTF-8",
                                   delay=False, utc=True)
app.logger.addHandler(handler)
handler.setFormatter(formatter)
