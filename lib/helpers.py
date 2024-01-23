# lib/helpers.py
from models.owner import Owner
from models.art import Art 
import ipdb

def helper_1():
    print("Performing useful function#1.")



def list_owners():
    owners = Owner.get_all()
    for owner in owners:
        print(owner)

def create_owner():
    name = input("Enter the owner's name: ")
    try:
        owner = Owner.create(name)
        print(f'Success: {owner}')
    except Exception as exc:
        print("Error creating owner: ", exc)

def get_owner_name_by_id(owner_id):
    owner = Owner.find_by_id(owner_id)
    return owner.name if owner else None

def list_owner_arts(owner_id):
    owner = Owner.find_by_id(owner_id)
    owner_arts = owner.arts()
    for art in owner_arts:
        print(art)
    if not owner_arts:
        print('Sorry, you have no arts to view!')

def add_new_art(owner_id, owner_name):
    print(f"Adding a new art for owner: {owner_name}")
    owner = Owner.find_by_id(owner_id)

    if owner:
        name = input("Enter art name: ")
        artist = input("Enter artist name: ")
        cost = input("Enter art cost: ")
        cost_int = int(cost)

        art = Art.create(owner_id, name, artist, cost_int)
        print(f"Art '{art.name}' added successfully!")






def exit_program():
    print("Goodbye!")
    exit()

# ipdb.set_trace()
