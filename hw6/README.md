# Homework 5: Social Network MOdels (Python 2.7.10)

For this assignment, you will create the data models used to store posts and supplementary user profile information. You will use these data models to implement the ability for users to create & edit their profiles, make new blog posts, view blog posts, and follow other users.

## Specifications

The following **required** functionality is :

Make the following enhancements to your templates for your social network:

* [x] Create a data model for posts. Ensure your model has all the needed fields and declare these fields to be of an appropriate field type. (E.g., dates should not be stored in a character field.)

* [x] Create a data model for the enhanced profile. Specifically, you need to create a model to store the user bio and profile image. This model will also need a field to reference the Django authentication module’s User model (so you will know which user the extended profile data is for).

* [x] Create a data model to keep track of who a user is following. This can be a separate model or it can be part of the enhance profile model, above.

* [x] Create form or model-form objects to process posts and profile creation/edits. Be sure to validate input parameters using these form (or model-form) objects.

Create routing and actions (in urls.py and views.py) to implement:
* [x] profile creation/editing,
* [x] profile viewing,
* [x] post creation,
* [x] global stream viewing,
* [x] following,
* [x] unfollowing, and
* [x] follower stream viewing.
Display posts in reverse-chronological order (newest ones first).

* [x] Eliminate all hard-coded URLs in your Python and templating code by using reverse URL resolution. Particularly, this means usage of the {% url 'location' %} template tag as well as the reverse() function in Python.


## Implementation

* [x] Clicking on the name of the user that created a post should now show that user’s profile page and permit the logged-in user to follow the posting user (or unfollow this user, if the logged-in user is already following)

* [x] When viewing the currently logged-in user’s profile, you must show, 
• current bio and photo,
• a form to allow the bio and photo to be edited (or created) – or a link to a page to permit the profile to be edited
• a list of the other users that the logged-in user is following which includes links to the followed users’ profile pages.

## Requirements

Your submission must also follow these requirements:

o The empty URL (i.e. http://localhost:8000) must route to the first page of yourapplication.

o Your application should not use any hard-coded absolute paths.

o Your application should run with Django 1.11.

o Your application should use the default Django database configuration based on a SQLite database file (named db.sqlite3) in your project directory.

o Your application should not crash as a result of any input sent to the server-side or
because of any actions the user performs.

• Your application should use template inheritance, reverse URL resolution, as well as complete validation of client-submitted data with Django Forms.

• You should not commit into your repo your database file or any images. Update your .gitignore file accordingly. The TAs will “migrate” before running your homework. Your image (media) folder should be someplace under the hw5 folder (just as in the course example).

• All tasks and features in the specification must be easily accomplishable using the user interface for your social network.

● Cite all external resources used and any additional notes you would like to convey to your grader in the README.md file. Be sure to let us know in README.md which version of Python you are using.


## Git Ignore 

.pyc files, db.sqlite3, editor swap files and system specific files (such as .DS_Store) are not included

## References

https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone

https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html

