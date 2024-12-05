import os

class Config:
    # 密钥，用于保护表单数据和会话数据
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secure_secret_key'

    # 数据库路径配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    
    # 禁用 SQLAlchemy 的跟踪修改功能以提升性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False
