#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.owner import Owner

Owner.drop_table()
Owner.create_table()


owner1 = Owner.create("John")
print(owner1)
owner2 = Owner.create("Anne")
print(owner2)

owner1.name = 'John'
owner1.update()

owner2.delete()






import ipdb
ipdb.set_trace()
