from flask import Flask

import settings
from ext import db
from apps.user.view import user_bp


def create_app():
    app = Flask(__name__,template_folder="../templates",static_folder="../static")
    app.config.from_object(settings.DevelopmentConfig)
    # 将SQLAlchemy这个db对象和app关联起来
    db.init_app(app)
    # 把蓝图对象注册到app里面
    app.register_blueprint(user_bp)
    print(app.url_map)
    return app
