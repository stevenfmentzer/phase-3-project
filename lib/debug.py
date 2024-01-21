#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.owner import Owner

Owner.drop_table()
Owner.create_table()


Owner.drop_table()
Owner.create_table()

    # Create seed data
owner1 = Owner.create("John")
owner2 = Owner.create("Anne")
owner3 = Owner.create('Bob')


import ipdb
ipdb.set_trace()
