import time

from bson.json_util import dumps
from flask import Blueprint, request

from component import mymysql

app = Blueprint('permission', __name__,
                url_prefix='/permission')

local_memory_token_record = {}


def record_2_local_memory(token, user_id):
    global local_memory_token_record
    local_memory_token_record[token] = {"timestamp": (time.time()), "user_id": user_id}


@app.route('/verification_token')
def verification_token():
    """
    验证token是否有效
    :return:
    """
    token = request.args.get("token")
    expire_day = 7  # 有效期7天
    if token in local_memory_token_record:
        local_memory_token_record_value = local_memory_token_record[token]
        if int(time.time()) < local_memory_token_record_value["timestamp"] + 7 * 24 * 60 * 60:
            return dumps([{"user_id": local_memory_token_record_value["user_id"]}])
    result = mymysql.execute(
        "select user_id from user_user_token where token = %(token)s and datediff(now(), date(update_datetime)) < %(expire_day)s",
        {
            "expire_day": expire_day,
            "token": token
        })
    for item in result:
        record_2_local_memory(token, item["user_id"])
        break
    return dumps(result)


# @app.route('/test_record_token')
# def test_record_token():
#     user_id = request.args.get("user_id")
#     token = request.args.get("token")
#     return record_token(user_id, token)
def record_token(user_id, token):
    """
    记录token
    :param user_id:
    :param token:
    :return:
    """
    query_condition = {
        "user_id": user_id,
        "token": token,
    }
    # 查询是否有记录,
    result = mymysql.execute("select user_id from user_user_token where user_id='%s'" % user_id)
    if not result or len(result) < 1:  # 没有记录时插入一条记录
        result = mymysql.execute("""
                insert into user_user_token(user_id, token) values (%(user_id)s, %(token)s)
            """, query_condition)
    else:  # 有记录时修改记录
        result = mymysql.execute("update user_user_token set token=%(token)s where user_id = %(user_id)s",
                                 query_condition)
    record_2_local_memory(token, user_id)
    return dumps(result)
