'''
This program deletes the current tables in the development
environment and then recreates fresh tables.
'''
from VirtualLineup import db

print("Setting up dev environment")
print("Dropping all tables")
db.drop_all()

print("Creating all tables")
db.create_all()

