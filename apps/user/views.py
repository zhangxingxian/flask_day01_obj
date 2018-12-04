from datetime import datetime

from flask import Blueprint

'''
实例化blueprint对象
    test = Blueprint(name='test', import_name='__name__')
    name='test' test在项目中唯一, 一般在开发中使用模块名称
注册蓝图对象
    app.register_blueprint(blueprint=test, url_prefix='/test')

    :param blueprint: The blueprint to register. 
        实例化蓝图对象
    :param url_prefix: Blueprint routes will be prefixed with this.
        访问路径的前缀
'''
user = Blueprint(name='user', import_name=__name__, static_url_path='/user', static_folder='static')


@user.route('/login')
def login():
    return '登陆'


#
# @user.route('/users/<int:page>/')
# def users(page):
#     print(page)
#     return '当前第%d页' % page


# @user.route('/users/<username>/')
# def usernm(username):
#     print(username)
#     return username


# @user.route('/users/<path:path>/')
# def userpath(path):
#     print(path)
#     return path


# 自定义路由
@user.route(r'/users/<date_regex("\d{4}"):year>/')
def userdate(year):
    print(type(year))
    return '%s' % year


from werkzeug.routing import BaseConverter


class DateRegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(DateRegexConverter, self).__init__(url_map)
        self.regex = args[0]

    def to_python(self, value):
        value = datetime.strptime(value, '%Y')
        return value


# 请求方式
@user.route('/method/', methods=['post', 'get'])
def methodtest(year):
    return '请求方式'
