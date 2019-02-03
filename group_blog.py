import os
from flask import Flask

# Create app
app = Flask(__name__)

# Load configuration
app.config.from_pyfile('config.py')

from views import *

if __name__ == '__main__':
    app.run(debug=True)