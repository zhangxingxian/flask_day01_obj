from flask import Blueprint

# 实例化蓝图对象
detail = Blueprint(name='detail', import_name=__name__, static_url_path='/user', static_folder='static')


@detail.route('/detail')
def detail_view():
    return '详情'
