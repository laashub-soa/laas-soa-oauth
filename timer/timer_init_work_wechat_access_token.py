from component import work_wechat
import config


def init_work_wechat_access_token():
    work_wechat = config.app_conf["work_wechat"]
    work_wechat["app_id"]

    work_wechat.select_access_token()
