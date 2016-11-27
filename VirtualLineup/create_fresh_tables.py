'''
This program deletes the current tables in the development
environment and then recreates fresh tables.

It also adds some basic stores, lines, shoppers to play around with.
'''
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sys import argv
from VirtualLineup import db
from VirtualLineup.mod_store.models import VirtualStore
from VirtualLineup.mod_virtualline.models import VirtualLine
from VirtualLineup.mod_virtualline.line_type import VirtualLineType
from VirtualLineup.mod_shopper.models import Shopper

store_names = [('Sephora', '94034'),      \
               ('Macy\'s', '94104'),      \
               ('Foot Locker', '93454'),  \
               ('Anthropologie', '94074')]

shoppers = [('jasonbo@gmail.com', 'password', 'Jason', 'Bournce'), \
            ('jamesbo@hotmail.com', 'password', 'James', 'Bond')]

def recreate_tables():
    print("Dropping all tables")
    db.drop_all()

    print("Creating all tables")
    db.create_all()

def create_sample_stores(session):
    for store in store_names:
        new_store = VirtualStore(store[0], store[1])
        new_store.is_live = True
        cashier_line = VirtualLine()
        new_store.lines.append(cashier_line)
        session.add(new_store)
    
    session.commit()    

def create_sample_shoppers(session):
    for sho in shoppers:
        new_shopper = Shopper(sho[0], sho[1])
        new_shopper.first_name = sho[2]
        new_shopper.last_name  = sho[3]
        session.add(new_shopper)
    
    session.commit()
    
if __name__ == "__main__":
    print("Setting up dev environment")    
    recreate_tables()
    engine = create_engine('postgresql+psycopg2://postgres:qazwsx123@localhost/VirtualLineup')
   
    Session = sessionmaker(bind=engine)
    session = Session()
    
    create_sample_stores(session)
    create_sample_shoppers(session)

