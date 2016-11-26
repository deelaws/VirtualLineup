from flask_sqlalchemy import SQLAlchemy
from VirtualLineup import db
from VirtualLineup.base_models import Base
from werkzeug.security import generate_password_hash, check_password_hash

user_name_max_length = 25

'''
This class is the abstraciton for a shopper in a store.
A shopper will enter a virtual line in the store and shop for goods.

This is essentially the user model.
'''
class Shopper(Base):
    __tablename__ = 'vshopper'

    '''
    Email address will be the username
    '''
    email = db.Column(db.String, unique=True, nullable=False)

    '''
    Encrypted password for the user.    
    '''
    password = db.Column(db.String, nullable=False)

    authenticated = db.Column(db.Boolean, default=False)

    first_name = db.Column(db.String(user_name_max_length),  nullable=True)
    last_name = db.Column(db.String(user_name_max_length),  nullable=True)

    test_account = db.Column(db.Boolean, default=False)

    def __init__(self, username, password):
        """Constructor"""
        self.email = username
        self.set_password(password)

    def set_password(self, password):
        """Set's the password for the user.
           It generates a hash of the password using werkzeug
        """
        print("password is", password)
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """ Check's whether the specified password is correct """
        print("checking password")
        return check_password_hash(self.password, password)

    def is_active(self):
        """True, as all users are active."""
        return True

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email