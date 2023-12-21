# School-Application
A School web application and a database model using flask and flask-SQLAlchemy.

## Requirements
1. On the home page (URI = "/"), (when we open it via the browser) displays an index page. The index page must display a table with the list of students currently enrolled. The HTML table should be the same as given below (Its id must be "all-students"). It should display an appropriate message if no student is enrolled. It should also have a button labeled "Add student".
2. If the user clicks the "Add student", your flask application should send a GET request to an endpoint "/student/create", which should display an HTML form. The HTML form should be the same as given below. Its id must be "create-form".
3. The HTML form should not have any other input elements.
4. If the user clicks the submit button, the browser should send a POST request to your flask application's "/student/create" URI. The flask application should then create a student object (with attributes roll number, first name and last name) and enrollments objects(s) (depending on the number of courses user selects) and add them into the database and, it should redirect to the home page (URI = "/") and the student should be added into the table.
5. If the roll number already exists, then, the user should be redirected to an HTML page, which should display an appropriate message and have a button to navigate back to the home page (URI = "/").
6. If the user clicks the "Update" button, your flask application should send a GET request to an endpoint "/student/<int:student id>/update", which should display an HTML form.
7. The HTML form should not have any other input elements.
8. If the user clicks the submit button, the browser should send a POST request to your flask application's "/student/<int:student id>/update" URI.
9. The flask application should then update the student and corresponding enrollments into the database and redirect to the home page (URI = "/").
10. If the user clicks the “Delete” button, your flask application should send a GET request to an end-point "/student/<int:student id>/delete", which should delete the student and all the corresponding enrollments from the database and redirect to the home page (URI = "/").
11. If the user clicks on the roll number of any row in the table in the home page of the flask application, the application should send a GET request to an endpoint "/student/<int:student id>", which should show all the information (student details and enrollment details) in an HTML page. The HTML page should also have a button labelled "Go Back" to navigate back to the home page (URI = "/"). There must be 2 HTML tables in this page, one for showing the personal details and the other for displaying the enrollment details.

## Database Description
1: student
2: course
3: enrollments

