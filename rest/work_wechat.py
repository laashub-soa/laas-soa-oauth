import json

from flask import Blueprint, request, redirect

import config
from exception import MyServiceException
from timer import init_work_wechat_access_token

app = Blueprint('work_wechat', __name__,
                url_prefix='/work_wechat')

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
    if not code:
        raise MyServiceException("缺失请求参数: code")
    # state = request.args.get("state")  # 通过校验state可以预防csrd攻击
    if not init_work_wechat_access_token.access_token:
        raise MyServiceException("access_token已失效, 请联系管理员")

    return redirect("/login?token=" + code)
