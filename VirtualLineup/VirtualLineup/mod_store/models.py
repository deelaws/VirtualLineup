from flask_sqlalchemy import SQLAlchemy
from VirtualLineup import db
from VirtualLineup.base_models import Base

store_name_max_length = 100

class VirtualStore(Base):
    __tablename__ = 'vstore'

    name = db.Column(db.String(store_name_max_length),  nullable=True)

    # Store Address
    street = db.Column(db.String,  nullable=True)

    city = db.Column(db.String,  nullable=True)

    province_state = db.Column(db.String,  nullable=True)
    
    country = db.Column(db.String, nullable=True)

    zipcode = db.Column(db.String(5), nullable=True)

    # Is the store located in a mall?
    in_mall = db.Column(db.Boolean,  nullable=True, default=False)

    # If the store is live, then it is visible to shoppers
    is_live = db.Column(db.Boolean,  nullable=True, default=False)

    # One to Many relationship with VirtualLine
    lines = db.relationship('VirtualLine', backref='store',
                            lazy='dynamic')

    def __init__(self, name, zip_code):
        self.name = name
        self.zipcode = zip_code
