create table user_user_token
(
    id              int auto_increment comment '自增主键'
        primary key,
    user_id         varchar(100) not null comment '用户id',
    token           varchar(100) not null comment '登录令牌',
    update_datetime timestamp    not null default current_timestamp on update current_timestamp comment '数据更新时间'
)
    comment '用户领域_用户_权限令牌';