from flask import Blueprint, session, g, request, \
                  render_template

from VirtualLineup import db
from VirtualLineup.mod_shopper.models import Shopper
from VirtualLineup.mod_store.models import VirtualStore

mod_shopper = Blueprint('shopper', __name__, url_prefix='/shopper')

'''
Displays the current profile of the user.
'''
@mod_shopper.route('/profile/<int:userid>', methods=['GET'])
def show_profile(userid):
    shopper = Shopper.query.get(userid)
    return render_template('shopper/profile.html', user=shopper)

'''
Displays dashboard to the user.
In the dashboard, user can enter into a line and perform other related
tasks i.e trade ticket, view open stores etc.
'''
@mod_shopper.route('/dashboard', methods=['GET'])
def display_dashboard():
    stores = VirtualStore.query.all()
    return render_template('shopper/dashboard.html', stores=stores)
