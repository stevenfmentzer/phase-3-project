# lib/helpers.py
from models.owner import Owner
from models.art import Art

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





def exit_program():
    print("Goodbye!")
    exit()
