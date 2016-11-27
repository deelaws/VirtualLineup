from flask import Blueprint, session, g

from VirtualLineup import db
from VirtualLineup.mod_store.models import VirtualStore

mod_store = Blueprint('store', __name__, url_prefix='store')

