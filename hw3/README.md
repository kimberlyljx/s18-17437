# Homework 3

In this homework, you will extend your first homework assignment to implement the calculator functions by sending web request to a Django application running server-side. The calculator should appear to work in (approximately) the same manner as it did your second homework. You must do the computations Python on the server, not in JavaScript in the browser

## Specifications

The following **required** functionality is completed:

* [] The calculator will use the front end that you wrote for the previous homework.
* [] The number displayed at all times is a single integer value. This value is initially zero (0)… unless the user attempts to divide by zero, in which case you should reset the state and display an error message using a JavaScript alert.
* [] The calculator does integer math (e.g. 9 ÷ 4 = 2).
* [] No operator precedence. Do the operations in the order they are encountered.

## Requirements

Your submission must also follow these requirements:

* [X] Your submission must follow all of the requirements specified in the last homework assignment.
* [X] You may not use any external libraries (e.g. jQuery, Bootstrap, etc.).
* [X] You may not use the JavaScript eval() function in the implementation of your calculator.
* [] Your calculator must be able to support numbers up to ±1,000,000. We will not test numbers
* [] Your Django application may not crash on any user input. If two (or more) operation buttons are clicked without a digit in between, you must not crash. The computation for this is up to you.
* [] Your application should run with Django 1.11. See the Django Quick Start guide posted on
Canvas for info on how to use pip to install the correct version. (The TAs use Django 1.11.)
* [] The empty URL (i.e. http://localhost:8000/ if the server is run on port 8000) must route to your
application’s main page in a cleared state.
* [] You are not to store anything in the database. The server should be **stateless**: the server may not
store any data between web requests. To meet this requirement your server will need to send extra data (in addition to the displayed calculator value) to the client with each response. The client will need to resubmit that extra data with its next request.
* [] Your application must run on the web server. The web browser must simply submit requests to the web server (after each button­ click) and display the response; the client may not use JavaScript or perform any processing of the calculator data.
* [] Your application may not crash as a result of any input sent to the server-side or because of any actions the user performs. Note that the user can send any data (malformed or otherwise) to the server, and you must anticipate and validate these requests.
* [] Cite all external resources used and any additional notes you would like to convey to your grader in the hw3/README.md file.
* [] Indicate in the hw3/README.md file which version of Python you are using (Python 2.7.x or Python 3.x), – i.e., give us the value for x. (Just run Python in the terminal to see the version.)

## Implementation

● You must do the computations Python on the server, not in JavaScript in the browser


## Git Ignore 

.pyc files, db.sqlite3, editor swap files and system specific files (such as .DS_Store) are not included

## Submisssion

Your submission should be turned in via Git in a directory called hw2 and should consist of an HTML file
called calculator.html, a JavaScript file called calculator.js, and associated assets (CSS andimages).

## References
- [GitIgnore Sample](https://github.com/CMU-Web-Application-Development/django-intro/blob/master/.gitignore)

## License

    Copyright [2018] [KIMBERLY LIM JINXIA]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.