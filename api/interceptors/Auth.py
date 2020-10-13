# -*- coding: utf-8 -*-

from application import app

@app.before_request
def before_request():
    return


@app.after_request
def after_request( response ):
    return response
