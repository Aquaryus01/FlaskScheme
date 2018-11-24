from flask import Blueprint
from ..model.User import User
from ..config import *
user_api = Blueprint('account_api', __name__)
User = User(connection())
@user_api.route("/account")
def accountList():
    return "list of accounts"