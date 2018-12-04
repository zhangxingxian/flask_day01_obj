import os

from flask import Blueprint, url_for, render_template

root_path = os.path.dirname(__file__)
static_file = os.path.join(root_path, 'static')

# 实例化一个蓝图对象

main = Blueprint(name='main', import_name=__name__, static_url_path='/main', static_folder=static_file)


@main.route('/index')
@main.route('/')
def index():
    return '首页'


# 反向解析
@main.route('/path')
def url_path():
    # 本app应用下方向解析
    # path = url_for('.index')
    # 跨app应用下反向解析 相等路径
    # path = url_for('user.login')
    # 跨app应用下反向解析 动态路由
    # year参数名称 必须是动态路径的名称
    # path = url_for('user.userdate', year='2018', _external=True)

    # 反向解析apps下的静态文件
    # path = url_for('static', filename='img/2.jpg', _external=True)

    # 反向解析app应用下的静态文件
    path = url_for('user.static', filename='img/1.jpg', _external=True)
    return path


@main.route('/temp/')
def temp_view():
    return render_template('temp.html', msg='hello', num=1)
