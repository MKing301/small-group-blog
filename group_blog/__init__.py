from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create app
app = Flask(__name__)

# Load configuration
app.config.from_pyfile('config.py')

# Create db
db = SQLAlchemy(app)

from group_blog import views