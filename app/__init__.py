from flask import Flask
from .config import DevConfig

# from flask_bootstrap import Bootstrap
# from config import config_options

#initializing app
app = Flask(__name__)

# setting up configuration
app.config,from_object (DevConfig)

from app import views