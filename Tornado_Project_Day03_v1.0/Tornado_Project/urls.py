# coding:utf-8

import os

from handlers import Passport, VerifyCode
from handlers.BaseHandler import StaticFileHandler

handlers = [
    (r"/api/imagecode", VerifyCode.ImageCodeHandler),
    (r"/api/smscode", VerifyCode.SMSCodeHandler),
    (r'^/api/register$', Passport.RegisterHandler),
    (r'^/api/login$', Passport.LoginHandler),
    (r'^/api/check_login$', Passport.CheckLoginHandler),
    (r"/(.*)", StaticFileHandler, dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html"))
]