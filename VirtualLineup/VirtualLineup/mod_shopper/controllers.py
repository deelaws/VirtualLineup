from flask import Blueprint, session, g

from VirtualLineup import db
from VirtualLineup.mod_shopper.models import Shopper


mod_shopper = Blueprint('shopper', __name__, url_prefix='shopper')
