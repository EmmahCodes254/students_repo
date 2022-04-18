from crypt import methods
from os import abort
from flask import Flask, render_template, request, redirect
from models import db, StudentModel


app = Flask(__name__)

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

# function to create a student
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        hobby = request.form.getlist('hobbies')
        hobbies = ",".join(map(str, hobby))
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        hobbies = hobbies
        country = request.form['country']

        students = StudentModel(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password,
            gender = gender,
            hobbies = hobbies,
            country = country
        )
        db.session.add(students)
        db.session.commit()
        return redirect('/')


# function to render index page with list of created students
@app.route('/', methods=['GET'])
def RetrieveList():
    students = StudentModel.query.all()
    return render_template('index.html', students = students)


# function edit a student
@app.route('/<int:id>/edit', methods = ['GET', 'POST'])
def update(id):
    students = StudentModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        db.session.delete(students)
        db.session.commit()
        if students:
            hobby = request.form.getlist('hobbies')
            hobbies = ",".join(map(str, hobby))
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            gender = request.form['gender']
            hobbies = hobbies
            country = request.form['country']

            students = StudentModel(
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password,
                gender = gender,
                hobbies = hobbies,
                country = country
            )
            db.session.add(students)
            db.session.commit()
            return redirect('/')
        return f"Student with id = {id} Does not exist "

    return render_template('update.html', students = students)


# function to delete a student
@app.route('/<int:id>/delete', methods = ['GET', 'POST'])
def delete(id):
    students = StudentModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if students:
            db.session.delete(students)
            db.session.commit()
            return redirect('/')
        abort(404)
    return render_template('delete.html')

if __name__ == "__main__":
    app.run()