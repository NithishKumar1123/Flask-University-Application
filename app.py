from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    roll_number = db.Column(db.String, unique = True, nullable = False)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String)
    courses = db.relationship("Course", secondary = "enrollments")

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    course_code = db.Column(db.String, unique = True, nullable = False)
    course_name = db.Column(db.String, nullable = False)
    course_description = db.Column(db.String)

class Enrollments(db.Model):
    __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    estudent_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable = False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable = False)

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index_page.html', students = students)

@app.route('/student/create', methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("student_create.html")
    else:
        roll = request.form["roll"]
        f_name = request.form["f_name"]
        l_name = request.form["l_name"]
        course_list = request.form.getlist("courses")
        data = Student.query.filter_by(roll_number = roll).all()
        if(data == []):
            new_student = Student(roll_number = roll, first_name = f_name, last_name = l_name)
            db.session.add(new_student)
            db.session.commit()
            if('course_1' in course_list):
                new_enrollment = Enrollments(estudent_id = new_student.student_id, ecourse_id = 1)
                db.session.add(new_enrollment)
            if('course_2' in course_list):
                new_enrollment = Enrollments(estudent_id = new_student.student_id, ecourse_id = 2)
                db.session.add(new_enrollment)
            if('course_3' in course_list):
                new_enrollment = Enrollments(estudent_id = new_student.student_id, ecourse_id = 3)
                db.session.add(new_enrollment)
            if('course_4' in course_list):
                new_enrollment = Enrollments(estudent_id = new_student.student_id, ecourse_id = 4)
                db.session.add(new_enrollment)
            db.session.commit()
            return redirect("/")
        else:
            return render_template("student_exist.html")

@app.route("/student/<int:student_id>/update", methods = ["GET", "POST"])
def update(student_id):
    if request.method == "GET":
        data = Student.query.filter_by(student_id = student_id)
        return render_template("student_update.html", student = data[0])
    else:
        f_name = request.form["f_name"]
        l_name = request.form["l_name"]
        course_list = request.form.getlist("courses")
        student = Student.query.filter_by(student_id = student_id).all()
        student[0].first_name = f_name
        student[0].last_name = l_name
        if('course_1' in course_list):
            enroll = Enrollments.query.filter_by(estudent_id = student_id, ecourse_id = 1).all()
            if(enroll == []):
                update_enrollment = Enrollments(estudent_id = student_id, ecourse_id = 1)
                db.session.add(update_enrollment)
        else:
            enroll = Enrollments.query.filter_by(estudent_id = student_id, ecourse_id = 1).all()
            if(enroll != []):
                db.session.delete(enroll[0])
        if('course_2' in course_list):
            enroll = Enrollments.query.filter_by(estudent_id = student_id, ecourse_id = 2).all()
            if(enroll == []):
                update_enrollment = Enrollments(estudent_id = student_id, ecourse_id = 2)
                db.session.add(update_enrollment)
        else:
            enroll = Enrollments.query.filter_by(estudent_id = student_id, ecourse_id = 2).all()
            if(enroll != []):
                db.session.delete(enroll[0])
        if('course_3' in course_list):
            enroll = Enrollments.query.filter_by(estudent_id = student_id, ecourse_id = 3).all()
            if(enroll == []):
                update_enrollment = Enrollments(estudent_id = student_id, ecourse_id = 3)
                db.session.add(update_enrollment)
        else:
            enroll = Enrollments.query.filter_by(estudent_id = student_id, ecourse_id = 3).all()
            if(enroll != []):
                db.session.delete(enroll[0])
        if('course_4' in course_list):
            enroll = Enrollments.query.filter_by(estudent_id = student_id, ecourse_id = 4).all()
            if(enroll == []):
                update_enrollment = Enrollments(estudent_id = student_id, ecourse_id = 4)
                db.session.add(update_enrollment)
        else:
            enroll = Enrollments.query.filter_by(estudent_id = student_id, ecourse_id = 4).all()
            if(enroll != []):
                db.session.delete(enroll[0])
        db.session.commit()
        return redirect("/")

@app.route("/student/<int:student_id>/delete")
def delete(student_id):
    enroll = Enrollments.query.filter_by(estudent_id = student_id).all()
    for row in enroll:
        db.session.delete(row)
    student = Student.query.filter_by(student_id = student_id).all()
    db.session.delete(student[0])
    db.session.commit()
    return redirect("/")

@app.route("/student/<int:student_id>")
def display(student_id):
    students = Student.query.filter_by(student_id = student_id).all()
    enroll = Enrollments.query.filter_by(estudent_id = student_id).all()
    courses = []
    for row in enroll:
        courses.append(Course.query.filter_by(course_id = row.ecourse_id).one())
    return render_template("student_display.html", students = students, courses = courses)

if __name__ == '__main__':
    app.run(debug = True)