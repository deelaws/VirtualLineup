from flask import Blueprint, session, g

from VirtualLineup import db
from VirtualLineup.mod_virtualline.models import VirtualLine, VirtualTicket

mod_virtual_line = Blueprint('vline', __name__, url_prefix='vline')