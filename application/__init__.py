# -*- coding: utf-8 -*-
"""
    File name           : __init__.py
    Author              : Derryn Edwards
    Date Created        : 2020/07/01
    Date Last Modified  : 2020/07/13
    Python Version      : 3.8
"""
# ==================================================================================================
# IMPORTS
# ==================================================================================================
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """
    Construct the core application
    """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        from . import routes # pylint: disable=W0611,C0415

        #Create tables for our models
        db.create_all()

        return app
