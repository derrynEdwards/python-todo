# -*- coding: utf-8 -*-
"""
    File name           : models.py
    Author              : Derryn Edwards
    Date Created        : 2020/07/01
    Date Last Modified  : 2020/07/13
    Python Version      : 3.8
"""
# ==================================================================================================
# IMPORTS
# ==================================================================================================
from . import db

class List(db.Model): # pylint: disable=R0903
    """
    Lists database model.
    """
    __tablename__ = 'lists'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(),
                     nullable=False)
    completed = db.Column(db.Boolean,
                          nullable=False,
                          default=False)
    tasks = db.relationship('Task',
                            backref='list',
                            lazy=True,
                            cascade='all, delete-orphan')

    def __repr__(self):
        return '<List {}>'.format(self.name)

class Task(db.Model): # pylint: disable=R0903
    """
    Tasks database model.
    """
    __tablename__ = 'tasks'
    id = db.Column(db.Integer,
                   primary_key=True)
    description = db.Column(db.String(),
                            nullable=False)
    completed = db.Column(db.Boolean,
                          nullable=False,
                          default=False)
    list_id = db.Column(db.Integer,
                        db.ForeignKey('lists.id'),
                        nullable=False)

    def __repr__(self):
        return '<Task {}>'.format(self.description)
