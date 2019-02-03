"""This is the configuration file for the application."""
import os

# To generate a secret key
# import secrets
# secrets.token_hex(16)
SECRET_KEY = os.environ.get('SECRET_KEY_LOCAL')
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
