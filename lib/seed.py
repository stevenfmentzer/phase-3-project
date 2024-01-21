#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.owner import Owner

def seed_database():
    Owner.drop_table()
    Owner.create_table()

    # Create seed data
    owner1 = Owner.create("John")


seed_database()
print("Seeded database")
