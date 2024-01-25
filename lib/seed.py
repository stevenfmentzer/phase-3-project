#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.owner import Owner
from models.museum import Museum
from models.exhibition import Exhibition
from models.art import Art
from models.request import Request


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

    # Art owned by John
    art1 = Art.create(1, "Abstract Fusion", "Artist A", 200000)
    art2 = Art.create(1, "Sculpture of Time", "Artist B", 180000)
    art3 = Art.create(1, "Digital Dreamscape", "Artist C", 150000)

    # Art owned by Anne
    art4 = Art.create(2, "Sunflowers", "Van Gogh", 250000)
    art5 = Art.create(2, "Water Lilies", "Monet", 220000)
    art6 = Art.create(2, "Dancers in Pink", "Degas", 180000)

    # Art owned by Bob
    art7 = Art.create(3, "Persistence of Memory", "Dalí", 300000)
    art8 = Art.create(3, "The Elephants", "Dalí", 280000)
    art9 = Art.create(3, "The Lovers", "Magritte", 200000)

    # Museums
    museum1 = Museum.create("Brooklyn Museum")
    museum2 = Museum.create("The Whitney")
    museum3 = Museum.create("MoMA")

    # Exhibition 1
    exhibition1_1 = Exhibition.create(
        "Modern Art Showcase", 1, 1, "2024-01-11", "2024-06-11"
    )
    exhibition1_2 = Exhibition.create(
        "Modern Art Showcase", 4, 1, "2024-01-11", "2024-06-11"
    )
    exhibition1_3 = Exhibition.create(
        "Modern Art Showcase", 7, 1, "2024-01-11", "2024-06-11"
    )
    request1_1 = Request.create(
        art_id=art1.id, owner_id=1, exhibition_name="Modern Art Showcase", approved=True
    )
    request1_2 = Request.create(
        art_id=art4.id, owner_id=2, exhibition_name="Modern Art Showcase", approved=True
    )
    request1_3 = Request.create(
        art_id=art7.id, owner_id=3, exhibition_name="Modern Art Showcase", approved=True
    )

    # Exhibition 2
    exhibition2_1 = Exhibition.create(
        "Impressionist Masterpieces", 2, 1, "2024-07-11", "2024-12-31"
    )
    exhibition2_2 = Exhibition.create(
        "Impressionist Masterpieces", 5, 1, "2024-07-11", "2024-12-31"
    )
    exhibition2_3 = Exhibition.create(
        "Impressionist Masterpieces", 8, 1, "2024-07-11", "2024-12-31"
    )
    request2_1 = Request.create(
        art_id=art2.id,
        owner_id=1,
        exhibition_name="Impressionist Masterpieces",
        approved=True,
    )
    request2_2 = Request.create(
        art_id=art5.id,
        owner_id=2,
        exhibition_name="Impressionist Masterpieces",
        approved=True,
    )
    request2_3 = Request.create(
        art_id=art8.id,
        owner_id=3,
        exhibition_name="Impressionist Masterpieces",
        approved=True,
    )

    # Exhibition 3
    exhibition3_1 = Exhibition.create(
        "Surrealist Wonders", 3, 2, "2024-01-11", "2024-06-11"
    )
    exhibition3_2 = Exhibition.create(
        "Surrealist Wonders", 6, 2, "2024-01-11", "2024-06-11"
    )
    exhibition3_3 = Exhibition.create(
        "Surrealist Wonders", 9, 2, "2024-01-11", "2024-06-11"
    )
    request3_1 = Request.create(
        art_id=art3.id, owner_id=1, exhibition_name="Surrealist Wonders", approved=True
    )
    request3_2 = Request.create(
        art_id=art6.id, owner_id=2, exhibition_name="Surrealist Wonders", approved=True
    )
    request3_3 = Request.create(
        art_id=art9.id, owner_id=3, exhibition_name="Surrealist Wonders", approved=True
    )

    # Exhibition 4
    exhibition4_1 = Exhibition.create(
        "Ancient Art Treasures", 1, 3, "2024-07-11", "2024-12-31"
    )
    exhibition4_2 = Exhibition.create(
        "Ancient Art Treasures", 5, 3, "2024-07-11", "2024-12-31"
    )
    exhibition4_3 = Exhibition.create(
        "Ancient Art Treasures", 9, 3, "2024-07-11", "2024-12-31"
    )
    request4_1 = Request.create(
        art_id=art1.id,
        owner_id=1,
        exhibition_name="Ancient Art Treasures",
        approved=False,
    )
    request4_2 = Request.create(
        art_id=art5.id,
        owner_id=2,
        exhibition_name="Ancient Art Treasures",
        approved=False,
    )
    request4_3 = Request.create(
        art_id=art9.id,
        owner_id=3,
        exhibition_name="Ancient Art Treasures",
        approved=False,
    )


seed_database()
print("Seeded database")
