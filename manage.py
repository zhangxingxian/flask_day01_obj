from flask_script import Manager, Server

from apps import create_app

# 核心对象
app = create_app()

'''
第一步 导入managed对象
    from flask_script import Manager, Server
第二部 实例化对象
    manager = Manager(app=app)
第三部 添加脚本命令
    manager.add_command('runserver', Server(port=9000, use_debugger=True))
'''
manager = Manager(app=app)
manager.add_command('runserver', Server(port=9000, use_debugger=True))

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

if __name__ == '__main__':
    manager.run()
