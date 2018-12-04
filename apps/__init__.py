from flask import Flask

from apps.admin.views import admin
from apps.detail.views import detail
from apps.main.views import main
from apps.user.views import user, DateRegexConverter

'''
注册蓝图对象
    app.register_blueprint(blueprint=test, url_prefix='/test')

    :param blueprint: The blueprint to register. 
        实例化蓝图对象
    :param url_prefix: Blueprint routes will be prefixed with this.
        访问路径的前缀
'''


def create_app():
    # 核心对象
    app = Flask(__name__)
    app.debug = True

    # 注册自定义转换器
    app.url_map.converters['date_regex'] = DateRegexConverter

    # 注册蓝图对象
    app.register_blueprint(blueprint=user, url_prefix='/user')
    app.register_blueprint(blueprint=main, url_prefix='/main')

    # 注册主页蓝图对象
    app.register_blueprint(blueprint=main, url_prefix='/')

    app.register_blueprint(blueprint=detail, url_prefix='/detail')
    app.register_blueprint(blueprint=admin, url_prefix='/admin')

    return app
