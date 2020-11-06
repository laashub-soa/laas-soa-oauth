from flask import Blueprint

app = Blueprint('ping', __name__,
                url_prefix='/ping')
"""
流程模板(结构)
"""


@app.route('')
def ping():
    return "pong"
