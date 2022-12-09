from flask import Blueprint, render_template, request, redirect

from apps.user.model import User

user_bp = Blueprint("user", __name__)
# 新建一个列表，列表里面保存的是一个个用户对象
users = []


@user_bp.route('/')
def user_center():
    return render_template("user/show.html", users=users)


@user_bp.route("/register", methods=['POST', 'get'])
def register():
    if request.method == "POST":
        # 获取post提交的数据
        username = request.form.get("username")
        print(username)
        password = request.form.get("password")
        print(password)
        repassword = request.form.get("repassword")
        print(repassword)
        phone = request.form.get("phone")
        # 先判断两次的密码是否一致
        if password == repassword:
            # 遍历一下列表里面的username,有没有和之前的相等的
            for u in users:
                if u.username == username:
                    # 如果存在已经相等的，就直接返回注册页面。并提示消息，用户已经注册
                    return render_template("user/register.html", msg="用户已经注册")
            # 创建user对象，并赋值
            user = User(username, password, phone)
            # 把对象装进列表里面
            users.append(user)
            # 如果遍历完，发现没有相同的名字，那就意味着注册成功个，并返回用户中心
            return redirect('/')
    return render_template('user/register.html')


@user_bp.route('/del')
def delete():
    # 获取传递的username
    username = request.args.get("username")
    # 根据username找到列表中的user
    for user in users:
        if user.username == username:
            users.remove(user)
            return redirect('/')
    return "删除失败"
    # 删除user
    pass


@user_bp.route("/login", methods=['POST', 'get'])
def login():
    return "用户登录"


@user_bp.route('/update', methods=["GET", "POST"])
def user_update():
    if request.method == "POST":
        realname= request.form.get("realname")
        username = request.form.get("username")
        password = request.form.get("password")
        phone = request.form.get("phone")
        for user in users:
            if user.username == realname:
                user.username = username
                user.phone = phone
            print(user)
            return "修改成功"
    else:
        # 是get请求
        username = request.args.get("username")
        for user in users:
            if user.username == username:
                return render_template('user/update.html',user= user)
    return render_template('user/register.html')


@user_bp.route("/logout", methods=['POST', 'get'])
def logout():
    return "用户退出"
