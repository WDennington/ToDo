from flask import Flask, render_template, request, redirect, url_for
from application.forms import TaskForm
from application import app, db
from application.models import Tasks


@app.route('/')
@app.route('/home')
def home():
    all_tasks = Tasks.query.all()
    output = ''
    return render_template("index.html", title="Home", all_tasks=all_tasks)
    #return render_template('layout.html')

@app.route('/create', methods=["GET","POST"])
def create():
    form = TaskForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_task = Tasks(description=form.description.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))

    return render_template("add.html", title="Create a Task", form=form)

@app.route("/complete/<int:id>")
def complete(id):
        task = Tasks.query.filter_by(id=id).first()
        task.completed = True
        db.session.commit()
        return redirect(url_for("create"))

@app.route("/incomplete/<int:id>")
def incomplete(id):
        task = Tasks.query.filter_by(id=id).first()
        task.completed = False
        db.session.commit()
        return f"Task {id} is now incomplete"

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    task_string = ''
    for item in all_tasks:
        task_string += "<br>"+ item.description
    return task_string

@app.route('/update/<name>')
def update(name):
    first_task = Tasks.query.first()
    first_task.description = name
    db.session.commit()
    return first_task.description

@app.route('/delete')
def delete():
    task_to_delete = Tasks.query.first()
    db.session.delete(task_to_delete)
    db.session.commit()
    return render_template('delete.html')

