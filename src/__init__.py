from flask import Flask

app = Flask(__name__)


#from .models import User
from .routes import routes
