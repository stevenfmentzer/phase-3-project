#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.owner import Owner
from models.museum import Museum
from models.exhibition import Exhibition
from models.exhibition import Art
from models.exhibition import Request
from unittest.mock import Mock


# Usage in testing
fake_art_instance = Art(id=1, name="Fake Artwork")
fake_request_instance = Request(id=1, description="Fake Request")
from models.art import Art

def seed_database():
    Owner.drop_table()
    Owner.create_table()

    # Create seed data
    owner1 = Owner.create("John")
    owner2 = Owner.create("Anne")
    owner3 = Owner.create('Bob')


seed_database()
print("Seeded database")