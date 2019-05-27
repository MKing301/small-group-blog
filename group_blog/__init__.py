from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from group_blog.config import Config


# Create app
app = Flask(__name__)
app.config.from_object(Config)

# Create db
db = SQLAlchemy(app)

# Set up encrpytion
bcrypt = Bcrypt(app)

# Create instance of login manager
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

from group_blog.users.routes import users
from group_blog.posts.routes import posts
from group_blog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
