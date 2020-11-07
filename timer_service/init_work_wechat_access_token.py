import logging
import threading
import time

import config
from component import work_wechat
from . import init_work_wechat_access_token

init_work_wechat_access_token.access_token = None
init_work_wechat_access_token.expires_in = 0
init_work_wechat_access_token.last_init_ok_time = 0
init_work_wechat_access_token.next_time = 0

logger = logging.getLogger(__name__)


def do_init_work_wechat_access_token():
    while True:
        try:
            time.sleep(init_work_wechat_access_token.next_time)
            logger.warning("init_work_wechat_access_token begging")
            config_work_wechat = config.app_conf["work_wechat"]
            corp_id = config_work_wechat["app_id"]
            corp_secret = config_work_wechat["secret"]

            access_token_info = work_wechat.select_access_token(corp_id, corp_secret)

            init_work_wechat_access_token.access_token = access_token_info["access_token"]
            init_work_wechat_access_token.expires_in = access_token_info["expires_in"]
            init_work_wechat_access_token.next_time = access_token_info["expires_in"] - 60 * 10  # 缓冲 10 分钟给管理员处理
            init_work_wechat_access_token.last_init_ok_time = int(time.time())

            time.sleep(1)  # 防止失控
        except Exception as e:
            logger.warning((str(e)))
            # 刷新access_token异常后, 每隔3秒钟再次刷新
            init_work_wechat_access_token.next_time = 3

            if int(time.time()) - init_work_wechat_access_token.last_init_ok_time >= \
                    init_work_wechat_access_token.expires_in:
                init_work_wechat_access_token.access_token = None  # 超时时将access_token设置为空


def run():
    logger.warning("init_work_wechat_access_token run")
    threading.Thread(target=do_init_work_wechat_access_token).start()
