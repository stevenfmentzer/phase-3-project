#!/usr/bin/env python3
# lib/debug.py
import ipdb
from models.__init__ import CONN, CURSOR
from models.owner import Owner
from models.art import Art
from models.museum import Museum
from models.exhibition import Exhibition
from models.request import Request




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

owner1 = Owner.create("John")
owner2 = Owner.create("Anne")
owner3 = Owner.create('Bob')
museum1 = Museum.create("Brooklyn Museum")
museum2 = Museum.create("The Whitney")
museum3 = Museum.create("MoMA")
exhibition1 = Exhibition.create("Figures of Speech", 1, 1, "2024-01-11", "2024-06-11")
exhibition2 = Exhibition.create("Figures of Speech 2", 2, 2, "2024-07-11", "2024-12-31")



art1 = Art.create(1, 'art name', "artist", 450000)
art2 = Art.create(2, 'Starry Night', "Van Gogh", 130090)
art3= Art.create(1, 'art2', 'artist', 2000 )
request1 = Request.create(1,1,'Figures of Speech1', True)




# owners  = CURSOR.execute('SELECT * FROM owners') - use to query owners when new ones added
ipdb.set_trace()



# import ipdb
ipdb.set_trace()
