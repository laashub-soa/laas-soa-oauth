import requests

from exception import MyServiceException


def select_access_token(corpid, corpsecret):
    """
    查询 access_token
    :param corpid:
    :param corpsecret:
    :return:
    """
    resp = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", {
        "corpid": corpid,
        "corpsecret": corpsecret,
    })
    result = resp.json()
    return {
        "access_token": result["access_token"],
        "expires_in": result["expires_in"],
    }


def select_user_info(access_token, code):
    """
    查询用户信息
    :param access_token:
    :param code:
    :return:
    """
    resp = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo", {
        "access_token": access_token,
        "code": code,
    })
    result = resp.json()
    if not result:
        raise MyServiceException("查询用户信息失败")
    if result["errcode"] != 0:
        raise MyServiceException("查询用户信息失败: %s" % result["errmsg"])
    if "UserId" not in result:
        raise MyServiceException("扫码用户不属于本应用内")

    return {
        "user_id": result["UserId"]
    }
