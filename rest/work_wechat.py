import json

from flask import Blueprint, request

import config

app = Blueprint('work_wechat', __name__,
                url_prefix='/user/work_wechat')

"""
微信登录
"""


@app.route('/select_login_config')
def select_login_config():
    """
    查询登录配置
    :return:
    """
    work_wechat = config.app_conf["work_wechat"]

    return json.dumps({
        "app_id": work_wechat["app_id"],
        "agent_id": work_wechat["agent_id"],
    })


@app.route('/auth-redirect')
def auth_redirect():
    code = request.args.get("code")
    state = request.args.get("state")

    return "pong"
