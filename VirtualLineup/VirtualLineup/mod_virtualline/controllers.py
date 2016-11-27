from flask import Blueprint, session, g

from VirtualLineup import db
from VirtualLineup.mod_virtualline.models import VirtualLine, VirtualTicket

mod_virtual_line = Blueprint('vline', __name__, url_prefix='/vline')

'''
Creates a ticket for a shopper in a virtual line.
'''
@mod_virtual_line.route('/create', methods=['GET', 'POST'])
def create_ticket():
    pass

@mod_virtual_line.route('/delete', methods=['DELETE'])
def delete_ticket():
    pass

@mod_virtual_line.route('/deactivate', methods=['GET', 'POST'])
def deactivate_ticket():
    pass

@mod_virtual_line.route('/delete', methods=['GET', 'POST'])
def trade_ticket():
    pass