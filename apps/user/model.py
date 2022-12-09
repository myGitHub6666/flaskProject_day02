class User:
    def __init__(self, username, password, phone=None):
        self.username = username
        self.password = password
        self.phone = phone

    def __str__(self):
        return self.username


# # 模型文件
# from datetime import datetime
#
# from ext import db
#
#
# class User1(db.Model):  # 这个user类就是user表
#     # db.Column（映射，约束） 映射表中的列
#     '''
#     类型：
#     db.Inteager int
#     '''
#     db.Column()
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(15), nullable=False)
#     password = db.Column(db.String(12), nullable=False)
#     phone = db.Column(db.String(11), nullable=False)
#     register_datetime = db.Column(db.Datetime, default=datetime.now)
#
#     def __str__(self):
#         return self.username
