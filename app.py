from flask import Flask, render_template, request, redirect
import db 


app = Flask(__name__)

db.init_db()

@app.route('/') 
def home():   # view 
    tasks = db.fetch_all_tasks() 
    return render_template('index.html', data = tasks)


@app.route("/add-task", methods= ["POST"])
def add_task():
    data = request.form['task_name']
    if data:
       db.add_task(data)
    return redirect('/')


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    db.delete_task(task_id)
    return redirect("/")


@app.route("/complete/<int:task_id>")
def make_complete(task_id):
    db.make_complete(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True) 