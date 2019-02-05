from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Create app
app = Flask(__name__)

# Load configuration
app.config.from_pyfile('config.py')

# Create db
db = SQLAlchemy(app)

# Set up encrpytion
bcrypt = Bcrypt(app)

# Create login manager
login_manager = LoginManager(app)

from group_blog import views