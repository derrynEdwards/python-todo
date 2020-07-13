# -*- coding: utf-8 -*-
"""
    File name           : config.py
    Author              : Derryn Edwards
    Date Created        : 2020/07/01
    Date Last Modified  : 2020/07/13
    Python Version      : 3.8
"""
# ==================================================================================================
# IMPORTS
# ==================================================================================================
from os import getenv
from dotenv import load_dotenv

load_dotenv()
class Config: # pylint: disable=R0903
    """ Set Flask configuration vars from .env file """

    #General Configs
    TESTING = getenv('TESTING')
    FLASK_DEBUG = getenv('FLASK_DEBUG')

    #Database
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    