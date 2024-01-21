#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.owner import Owner

def seed_database():
    Owner.drop_table()
    Owner.create_table()

    # Create seed data
    owner1 = Owner.create("John")
    owner2 = Owner.create("Anne")
    owner3 = Owner.create('Bob')


seed_database()
print("Seeded database")
