#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.owner import Owner
from models.museum import Museum
from models.exhibition import Exhibition
from models.art import Art
from models.request import Request


# fake_request_instance = Request(id=1, description="Fake Request")
# fake_request_instance2 = Request(id=2, description="Fake Request")


def seed_database():
    Owner.drop_table()
    Owner.create_table()
    Museum.drop_table()
    Museum.create_table()
    Exhibition.drop_table()
    Exhibition.create_table()
    Request.drop_table()
    Request.create_table()
    Art.drop_table()
    Art.create_table()

    # Create seed data
    owner1 = Owner.create("John")
    owner2 = Owner.create("Anne")
    owner3 = Owner.create("Bob")

    museum1 = Museum.create("Brooklyn Museum")
    museum2 = Museum.create("The Whitney")
    museum3 = Museum.create("MoMA")

    exhibition1 = Exhibition.create(
        "Figures of Speech", 1, 1, "2024-01-11", "2024-06-11"
    )
    exhibition2 = Exhibition.create(
        "Figures of Speech 2", 2, 2, "2024-07-11", "2024-12-31"
    )

    art1 = Art.create(1, "Mona Lisa", "Da Vinci", 400000)
    art2 = Art.create(2, "Starry Night", "Van Gogh", 130090)
    art2 = Art.create(2, "Starry Night 2", "Van Gogh", 130090)
    art2 = Art.create(2, "Starry Night 3", "Van Gogh", 130090)

    # request1 = Request(art_id=1, owner_id=1, exhibition_name=1, approved=True)
    request1 = Request.create(1, 1, "Figures of Speech", False)
    request2 = Request.create(2, 2, "Figures of Speech", False)
    request3 = Request.create(3, 2, "Figures of Speech", False)


seed_database()
print("Seeded database")
