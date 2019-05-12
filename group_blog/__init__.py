import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


# Create app
app = Flask(__name__)

# Configure Mail
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": os.environ.get('MAIL_USERNAME'),
    "MAIL_PASSWORD": os.environ.get('MAIL_PASSWORD')
}

app.config.update(mail_settings)
mail = Mail(app)

# Load configuration
app.config.from_pyfile('config.py')

# Create db
db = SQLAlchemy(app)

# Set up encrpytion
bcrypt = Bcrypt(app)

# Create instance of login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from group_blog import views
