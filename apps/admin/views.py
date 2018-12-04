from flask import Blueprint


# 实例化蓝图对象
admin = Blueprint(name='admin', import_name=__name__, static_url_path='/user', static_folder='static')


@admin.route('/')
def ad():
    return '站点'