# Small Group Blog Project

This _**Small Group Blog Web Application**_ can be used as a platform for people to share content for a specific topic(s).  This app contains the following functionality:

* User Registration
* User Login
* User Password Reset
* Update Profile Picture
* Create a Post
* View All Posts
* Update and Delete Posts (Users can only update or delete post they created)


# Requirements
* Ubuntu 18.04
* Python 3
* [Virtual Environment for Python3](https://docs.python.org/3/library/venv.html)


# Resources

* [Python Flask Tutorial](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=1)


# Installation

Clone [repository](https://github.com/MKing301/small-group-blog.git)
`cd` to small-group-blog
Type `source venv/bin/activate`
Type `pip install -r requirements.txt`

# Run the program (local)

Type `python3 run.py`

You will see something like the following...

```
Serving Flask app "group_blog" (lazy loading)
Environment: production
WARNING: Do not use the development server in a production environment.
Use a production WSGI server instead.
Debug mode: off
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Open a browser and type `localhost:5000` to access the application

# Exit the program

In the terminal, type `CTRL + C`
Type `deactivate` and click `ENTER`
