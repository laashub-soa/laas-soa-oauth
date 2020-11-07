from flask import Blueprint, request

app = Blueprint('work_wechat', __name__,
                url_prefix='/user/work_wechat')
"""
流程模板(结构)
"""


@app.route('/auth-redirect')
def auth_redirect():
    print("get: ", request.args, "post: ", request.get_data())
    return "pong"
