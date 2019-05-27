"""This is the configuration file for the application."""
import os

# To generate a secret key
# import secrets
# secrets.token_hex(16)

class Config:
   SECRET_KEY = os.environ.get('SECRET_KEY_LOCAL')
   SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USE_SSL = False
   MAIL_USERNAME =  os.environ.get('MAIL_USERNAME')
   MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

