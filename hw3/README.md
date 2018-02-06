# Homework 3 (Python 2.7.10)

In this homework, you will extend your first homework assignment to implement the calculator functions by sending web request to a Django application running server-side. The calculator should appear to work in (approximately) the same manner as it did your second homework. You must do the computations Python on the server, not in JavaScript in the browser

## Specifications

The following **required** functionality is completed:

* [x] The calculator will use the front end that you wrote for the previous homework.
* [x] The number displayed at all times is a single integer value. This value is initially zero (0)… unless the user attempts to divide by zero, in which case you should reset the state and display an error message
* [x] The calculator does integer math (e.g. 9 ÷ 4 = 2).
* [x] No operator precedence. Do the operations in the order they are encountered.

## Requirements

Your submission must also follow these requirements:

* [X] Your submission must follow all of the requirements specified in the last homework assignment.
* [X] You may not use any external libraries (e.g. jQuery, Bootstrap, etc.).
* [X] You may not use the JavaScript eval() function in the implementation of your calculator.
* [x] Your calculator must be able to support numbers up to ±1,000,000. We will not test numbers
* [x] Your Django application may not crash on any user input. If two (or more) operation buttons are clicked without a digit in between, you must not crash. The computation for this is up to you.
* [x] Your application should run with Django 1.11. See the Django Quick Start guide posted on
Canvas for info on how to use pip to install the correct version. (The TAs use Django 1.11.)
* [x] The empty URL (i.e. http://localhost:8000/ if the server is run on port 8000) must route to your
application’s main page in a cleared state.
* [x] You are not to store anything in the database. The server should be **stateless**: the server may not
store any data between web requests. To meet this requirement your server will need to send extra data (in addition to the displayed calculator value) to the client with each response. The client will need to resubmit that extra data with its next request.
* [x] Your application must run on the web server. The web browser must simply submit requests to the web server (after each button­ click) and display the response; the client may not use JavaScript or perform any processing of the calculator data.
* [] Your application may not crash as a result of any input sent to the server-side or because of any actions the user performs. Note that the user can send any data (malformed or otherwise) to the server, and you must anticipate and validate these requests.
* [x] Cite all external resources used and any additional notes you would like to convey to your grader in the hw3/README.md file.
* [x] Indicate in the hw3/README.md file which version of Python you are using (Python 2.7.x or Python 3.x), – i.e., give us the value for x. (Just run Python in the terminal to see the version.)

## Implementation

● You must do the computations Python on the server, not in JavaScript in the browser

● Refresh in browser result in calculator reset

● Provide error messages instead of Django exception error pages.

● You press a button on the browser, which sends a request to the server. Then, the server sends back a response, which is displayed on your browser. 

● Page is reloaded after each click

● Form and hidden fields are used.

## Git Ignore 

.pyc files, db.sqlite3, editor swap files and system specific files (such as .DS_Store) are not included

## References

- [GitIgnore Sample](https://github.com/CMU-Web-Application-Development/django-intro/blob/master/.gitignore)
