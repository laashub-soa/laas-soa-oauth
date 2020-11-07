from flask import Blueprint

app = Blueprint('work_wechat', __name__,
                url_prefix='/user/work_wechat')
"""
流程模板(结构)
"""


@app.route('/auth-redirect')
def auth_redirect():
    return "pong"
