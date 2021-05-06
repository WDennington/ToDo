from flask import Flask, render_template

from application import app, db
from application.models import Task


@app.route('/')
@app.route('/home')
def home():
    all_tasks = Task.query.all()
    output = ''
    return render_template("index.html", title="Home", all_tasks=all_tasks)
    return render_template('layout.html')

@app.route('/create')
def create():
    new_task = Task(description="Task added", complete=False)
    db.session.add(new_task)
    db.session.commit()
    return "New task added"

@app.route('/read')
def read():
    all_tasks = Task.query.all()
    task_string = ''
    for item in all_tasks:
        task_string += "<br>"+ item.description
    return task_string

@app.route('/update/<name>')
def update(name):
    first_task = Task.query.first()
    first_task.description = name
    db.session.commit()
    return first_task.description

@app.route('/delete')
def delete():
    game_to_delete = Games.query.first()
    db.session.delete(game_to_delete)
    db.session.commit()
    return render_template('delete.html')

