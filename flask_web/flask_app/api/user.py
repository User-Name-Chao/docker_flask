import random

from flask import Blueprint, jsonify, session, render_template, request

from flask_app.models import User

user_blue = Blueprint('user_blue', __name__)


def init_public(app):
    app.register_blueprint(blueprint=user_blue)


@user_blue.route('/', methods=["GET", "POST"])
def hello_world():
    """
    :return:
    """
    return 'hello world!'


@user_blue.route('/sign_user', methods=["POST"])
def sign_user():
    """
    :return:
    """
    user_id = session.get('user_id')
    phone = request.form.get("phone")
    if phone:
        code = ''.join(random.choices(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], k=6))
        # 在这发送短信验证码（code）操作，返回发送结果。
        # 短信发送成功使用当前登录的用户user_id当key将验证码存入缓存等待用户收到后填写提交验证，或者直接将验证码返回给前端由前端在用户输入完成后进行校验。
        session[user_id] = code
        print('-----------', session.get(user_id))
        return jsonify({"msg": "ok", "status": 200, "code": code})
    return jsonify({"msg": "error", "status": 400})


@user_blue.route('/profile', methods=["GET"])
def profile():
    """
    :return:
    """
    data = {}
    user_id = request.args.get("user_id")
    if user_id:
        user = User.query.filter(User.user_id == user_id).first()
        data['id'] = user.user_id
        data['first_name'] = user.name
        data['last_name'] = user.name
        return jsonify({"msg": "ok", "status": 200, "data": data})
    return jsonify({"msg": "error", "status": 400})
