from flask_sqlalchemy import SQLAlchemy
from VirtualLineup import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    '''
    Lets the models that inherit define their own primary key
    '''
    
    id            = db.Column(db.Integer,   primary_key=True)

    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())

    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                            onupdate=db.func.current_timestamp())