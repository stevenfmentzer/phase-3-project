#!/usr/bin/env python3
# lib/debug.py
import ipdb

from models.__init__ import CONN, CURSOR
from models.owner import Owner

Owner.drop_table()
Owner.create_table()
# ipdb.set_trace()



Owner.drop_table()
Owner.create_table()

    # Create seed data
owner1 = Owner.create("John")

owner2 = Owner.create("Anne")
owner3 = Owner.create('Bob')

# owners  = CURSOR.execute('SELECT * FROM owners') - use to query owners when new ones added
ipdb.set_trace()



# import ipdb
ipdb.set_trace()
