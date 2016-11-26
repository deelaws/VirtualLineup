from flask_sqlalchemy import SQLAlchemy
from VirtualLineup import db
from VirtualLineup.base_models import Base

store_name_max_length = 100

'''
This class abstracts a customer lineup inside of a store.
A VirtualLine is associated with only one store, but one store can have
many different types of lines.
'''
class VirtualLine(Base):
    __tablename__ = 'vline'
    
    # Foreign key to mod store
    # Many to One relationship with vstore.
    # store = 

    # Line can have a many Virtual Tickets
    # One to many relationship with vtickets
    # vector_of_tickets = perhaps this ought to be declared inside VirtualTicket class

    # Current capacity represents the amount of non-expired tickets in the
    # virtual line.
    current_capacity = db.Column(db.Integer, default=0)

    # Max capacity represents the maximum amount of non-expired tickets the
    # virtual line can contain. This value should be configurable.
    max_capacity = db.Column(db.Integer, default=5000)

'''
This class abstracts the presence of a user in store line.
To enter a virtual line, the user needs a ticket. This ticket can also be
traded with other shoppers to get ahead in the line for money or tokens.

VirtualTicket is essentially an abstraction between a store line and a shopper.
'''
class VirtualTicket(Base):
    __tablename__ = 'vticket'

    # Some tickets can be tradeable with other shoppers for money.
    tradeable = db.Column(db.Boolean, default=False)

    # Service time is the time when the ticketing agent, i.e cashier
    # customer service rep will provide the service to a shopper.
    # We will always store all the times as UTC standard time.
    service_time = db.Column(db.DateTime,  default=None)

    # If a ticket has gone past its service time, it has expired
    expired = db.Column(db.Boolean, default=False)

    # The shopper who is the owner of this ticket
    # shopper = db.relationship

    # The virtual line in which the ticket is used.
    # store = db.RelationShip