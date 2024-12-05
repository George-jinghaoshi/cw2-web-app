import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# 初始化扩展
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    # 显式指定模板文件夹的路径
    app = Flask(__name__, template_folder=os.path.abspath('templates'), static_folder=os.path.abspath('static'))
    
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # 配置登录视图
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'
    
    # 注册蓝图
    from app.routes import main
    app.register_blueprint(main)

    # 调试信息：打印模板目录的内容
    print("Templates directory content:", os.listdir(os.path.abspath('templates')))


    return app
