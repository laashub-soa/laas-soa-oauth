服务单独部署, 与soa服务共享数据库

soa服务查询共享数据库的同类表查询是否登录, 以及判断是否有权限

当然也支持通过接口判断是否有权限以及获取用户名

请求携带token, 去oauth服务中校验token, 推断出用户

# 功能

## 用户

接入方式

钉钉/企业微信/用户名-密码/ldap

## 角色

用户集

## 权限

### 菜单权限

### API权限

# 为什么要独立出来这样一个服务?

因为这种认证业务在很多业务里面都是共用的, 例如 sda、sua

暂时以soa项目为母项目进行发展



# 使用形式

如果是通过用户名-密码形式注册/登录则传递用户名-密码到oauth服务进行注册-登录

如果是通过企业微信/钉钉形式注册/登录则设置回调地址指向oauth服务, oauth服务接收回调, 存储 key:access_token 以及access_token所对应的用户信息, 接收后端请求并响应access_token和用户信息

