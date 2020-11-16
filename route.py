def init(app):
    from rest import ping
    from rest import work_wechat
    from rest import permission

    # 注册路由
    app.register_blueprint(ping.app)
    app.register_blueprint(work_wechat.app)
    app.register_blueprint(permission.app)
