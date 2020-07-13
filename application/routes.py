# -*- coding: utf-8 -*-
"""
    File name           : routes.py
    Author              : Derryn Edwards
    Date Created        : 2020/07/01
    Date Last Modified  : 2020/07/13
    Python Version      : 3.8
"""
# ==================================================================================================
# IMPORTS
# ==================================================================================================
from flask import render_template, request, jsonify, abort, redirect
from flask import current_app as app
from .models import db, Task, List

@app.route('/')
def index():
    """
    Handles index page.
    """
    return redirect('/lists/')

@app.route('/lists/')
def lists():
    """
    Renders the TO-DO Lists.
    """
    return render_template('index.html',
                           lists=List.query.order_by('id').all(),
                           active_list='')

@app.route('/lists/<list_id>')
def list_tasks(list_id):
    """
    Renders the TO-DO Lists with respective Tasks.
    """
    return render_template('index.html',
                           lists=List.query.order_by('id').all(),
                           active_list=List.query.get(list_id),
                           tasks=Task.query.filter_by(list_id=list_id).order_by('id').all())

@app.route('/create-todo', methods=['POST'])
def create_task(): # pylint: disable=R1710
    """
    Receives form data and inserts new Task into database.
    """
    error = False
    body = {}

    form_description = request.get_json()['description']
    list_id = request.get_json()['list_id']

    try:
        if form_description and list_id:
            task = Task(description=form_description,
                        list_id=list_id)
            db.session.add(task)
            db.session.commit()
            body['description'] = task.description
    except Exception as err: # pylint: disable=W0703
        db.session.rollback()
        error = True
        print(err)
    finally:
        db.session.close()

    if error:
        abort(400)
    else:
        return jsonify(body)

@app.route('/create-list', methods=['POST'])
def create_list(): # pylint: disable=R1710
    """
    Receives form data and inserts new List into database.
    """
    error = False
    body = {}
    form_name = request.get_json()['name']

    try:
        if form_name:
            new_list = List(name=form_name)
            db.session.add(new_list)
            db.session.commit()
            body['name'] = new_list.name
    except Exception as err: # pylint: disable=W0703
        db.session.rollback()
        error = True
        print(err)
    finally:
        db.session.close()

    if error:
        abort(400)
    else:
        return jsonify(body)

@app.route('/<todo_id>/set-completed', methods=['POST'])
def complete_task(todo_id): # pylint: disable=R1710
    """
    Updates tasks as completed or not completed in the database.
    """
    error = False
    body = {}

    try:
        #Variable to check if all tasks belonging to the list is completed
        all_completed = True
        completed = request.get_json()['completed']
        todo = Task.query.get(todo_id)
        #Save the list_id of the task
        list_id = todo.list_id
        todo.completed = completed
        #Get all the tasks existing in the same list
        all_todo = Task.query.filter_by(list_id=list_id).all()
        #If the task is set to 'completed=False', we set the whole list as not completed
        if not todo.completed:
            all_completed = False
        else:
        #if the current task was set to completed, we check the rest of the tasks in the list
            for task in all_todo:
                if not task.completed:
                    all_completed = False
                    break
        #Get the current list
        this_list = List.query.get(list_id)
        #If the list was set as completed, but one task was set as not completed, we set
        #the whole list as not completed; Else if all tasks in the list are completed
        #and the list was previously as not completed, we set the list as completed.
        if this_list.completed:
            if not all_completed:
                this_list.completed = False
        else:
            if all_completed:
                this_list.completed = True

        db.session.commit()

        body = {
            'success': True
        }
    except Exception as err: # pylint: disable=W0703
        db.session.rollback()
        error = True
        print(err)
    finally:
        db.session.close()

    if error:
        abort(400)
    else:
        return jsonify(body)

@app.route('/<list_id>/set-list-completed', methods=['POST'])
def complete_list(list_id): # pylint: disable=R1710
    """
    Updates all tasks as completed or not completed in the database base on list completion.
    """
    error = False
    body = {}

    try:
        completed = request.get_json()['completed']
        todo_list = List.query.get(list_id)
        todo_list.completed = completed
        #Get all the tasks related to the list_id and mark them all as completed or not completed.
        todo = Task.query.filter_by(list_id=list_id).all()
        for task in todo:
            task.completed = completed
        db.session.commit()

        body = {
            'success': True
        }
    except Exception as err: # pylint: disable=W0703
        db.session.rollback()
        error = True
        print(err)
    finally:
        db.session.close()

    if error:
        abort(400)
    else:
        return jsonify(body)

@app.route('/<todo_id>/delete-task', methods=['DELETE'])
def delete_task(todo_id): # pylint: disable=R1710
    """
    Deletes the task.
    """
    error = False
    body = {}

    try:
        todo = Task.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()

        body = {
            'success': True
        }
    except Exception as err: # pylint: disable=W0703
        db.session.rollback()
        error = True
        print(err)
    finally:
        db.session.close()

    if error:
        abort(400)
    else:
        return jsonify(body)

@app.route('/<list_id>/delete-list', methods=['DELETE'])
def delete_list(list_id): # pylint: disable=R1710
    """
    Deletes the list and all related tasks.
    """
    error = False
    body = {}

    try:
        todo_list = List.query.get(list_id)
        db.session.delete(todo_list)
        db.session.commit()
        body = {
            'success': True
        }
    except Exception as err: # pylint: disable=W0703
        db.session.rollback()
        error = True
        print(err)
    finally:
        db.session.close()

    if error:
        abort(400)
    else:
        return jsonify(body)



# Error Handling Pages
@app.errorhandler(404)
def not_found_error(error):
    """
    Returns 404 Template
    """
    print(error)
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Returns 500 Template
    """
    print(error)
    db.session.rollback()
    return render_template('500.html'), 500
