#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.owner import Owner
from models.art import Art


def seed_database():
    Owner.drop_table()
    Owner.create_table()

    # Create seed data
    owner1 = Owner.create("John")
    owner2 = Owner.create("Anne")
    owner3 = Owner.create("Bob")

    art1 = Art.create(1, "Mona Lisa", "Da Vinci", 400000)
    art2 = Art.create(2, "Starry Night", "Van Gogh", 130090)


seed_database()
print("Seeded database")
