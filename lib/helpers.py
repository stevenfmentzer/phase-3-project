# lib/helpers.py
from models.owner import Owner

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


def exit_program():
    print("Goodbye!")
    exit()
