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

def seed_database():
    Owner.drop_table()
    Owner.create_table()
    Museum.drop_table()
    Museum.create_table()
    Exhibition.drop_table()
    Exhibition.create_table()

    # Create seed data
    owner1 = Owner.create("John")
    owner2 = Owner.create("Anne")
    owner3 = Owner.create('Bob')

    museum1 = Museum.create("Brooklyn Museum")
    museum2 = Museum.create("The Whitney")
    museum3 = Museum.create("Guggenheim")    

    exhibition1 = Exhibition.create('Figures of Speech', 1, 1, "2023-1-12", "2023-11-12")

seed_database()
print("Seeded database")