# -*- coding: utf-8 -*-
from application import app
from flask import Blueprint

from common.components.helper.DateHelper import DateHelper

route_index = Blueprint('index_page', __name__)

@route_index.route("/")
def index():
    return "APP_NAME：{0} VERSION：{1} APP：API {2}"\
        .format( app.config.get("APP_NAME"),app.config.get("APP_VERSION"), DateHelper.getCurrentTime() )