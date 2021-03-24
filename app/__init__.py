#4th code for  init and run
from flask import Flask

app = Flask(__name__)

from app.main.index import main as main #cuz file name is index.py

app.register_blueprint(main) #linking files