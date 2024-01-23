#!/usr/bin/env python3
# lib/debug.py
import ipdb
from models.__init__ import CONN, CURSOR
from models.owner import Owner
from models.art import Art
from models.request import Request


Owner.drop_table()
Owner.create_table()
Art.drop_table()
Art.create_table()

owner1 = Owner.create("John")
owner2 = Owner.create("Anne")
owner3 = Owner.create("Bob")


art1 = Art.create(1, "art name", "artist", 450000)


# owners  = CURSOR.execute('SELECT * FROM owners') - use to query owners when new ones added
ipdb.set_trace()


# import ipdb
ipdb.set_trace()
