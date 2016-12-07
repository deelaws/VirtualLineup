from flask import Blueprint, session, g

from VirtualLineup import db
from VirtualLineup.mod_store.models import VirtualStore

mod_store = Blueprint('store', __name__, url_prefix='/store')

'''
Creates a ticket for a shopper in a virtual line.
'''
@mod_store.route('/get', methods=['GET'])
def get_stores():
    # Return all stores in our DB
    pass


