"""
The flask application package.
"""
import os, sys
from flask import Flask, g, session

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:qazwsx123@localhost/VirtualLineup'

db = SQLAlchemy(app)

from VirtualLineup.mod_shopper.controllers import mod_shopper
from VirtualLineup.mod_store.controllers import mod_store
from VirtualLineup.mod_virtualline.controllers import mod_virtual_line

app.register_blueprint(mod_shopper)
app.register_blueprint(mod_store)
app.register_blueprint(mod_virtual_line)

import VirtualLineup.views