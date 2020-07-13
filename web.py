# -*- coding: utf-8 -*-
"""
    File name           : web.py
    Author              : Derryn Edwards
    Date Created        : 2020/07/01
    Date Last Modified  : 2020/07/13
    Python Version      : 3.8
"""
# ==================================================================================================
# IMPORTS
# ==================================================================================================
from application import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    