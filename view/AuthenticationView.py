from flask import request, session
from werkzeug.utils import redirect
from services.LdapService import LdapService as ldapService

'''
@Function Authenticate users access
@Author Jiage
@Date 2022-02-03
'''
class AuthenticationView:
    def __init__(self):
        pass

    @staticmethod
    def auth(app):
        ls = ldapService(app)
        if request.path == "/login" and request.method == "POST":
            userName = request.form['username']
            password = request.form['password']
            if ls.isAuth(userName, password):
                session["userid"] = userName
                return redirect("/")
        if request.path == "/login":
            return None
        if request.path.startswith("/static"):
            return None
        if not session.get("userid"):
            return redirect("/login")
        return None
