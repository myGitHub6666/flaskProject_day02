class Config:
    DEBUG = True
    # 连接数据库
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flaskday05'
    # 默认是True 默认会追踪对象的修改并发送信号，这样会占用更多的内存
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 调试模式打开
    SQLALCHEMY_ECHO = True


class DevelopmentConfig(Config):
    EVN = "development"


class ProductionConfig(Config):
    EVN = "production"
    DEBUG = False
