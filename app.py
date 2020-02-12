from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# /// is relative path, //// is absolute path
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        taskContent = request.form['content']
        new_task = Todo(content=taskContent)

        try:
            db.session.add(new_task)
            db.session.commit()
            db.session.refresh(new_task)  # added from stack overflow
            id = new_task.id              # added from stack overflow
            return redirect('/?action=insert&id=' + str(id))
        except IOError:
            return "There was an issue adding your task."  
    else:  # it's GET, not generating a form, just loading page
        tasksToGet = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.htm", taskstoget=tasksToGet) 
    # render_template knows to look in templates folder
    # "template inheritance" - "master html file" - inherit
    # from each other page, and change what's relevant.


@app.route('/delete/<int:id>')
def delete(id):
    taskToDelete = Todo.query.get_or_404(id)

    try:
        db.session.delete(taskToDelete)
        db.session.commit()
        return redirect('/?action=delete&id=' + str(id))
    except IOError:
        return "there was a delete problem"

@app.route('/modify/<int:id>')
def modify(id):
    return redirect('/?action=modify&id=' + str(id))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    taskToUpdate = Todo.query.get_or_404(id)

    if request.method == 'POST':  # form has been submitted, get value
        # task.content = request.form['content']
        taskToUpdate.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/?action=update&id=' + str(id))
        except IOError:
            return 'There was an issue updating your task.'
    else:  # form not submitted, just show page
        print("About to update the entry for " + taskToUpdate.content + "...")
        # return render_template('update.html', tasktoupdate=taskToUpdate)
        return render_template("index.htm", tasktoupdate=taskToUpdate) 


if __name__ == "__main__":
    app.run(debug=True)