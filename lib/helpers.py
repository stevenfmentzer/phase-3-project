# lib/helpers.py
from models.owner import Owner

def helper_1():
    print("Performing useful function#1.")




def list_owners():
    owners = Owner.get_all()
    for owner in owners:
        print(owner)



def exit_program():
    print("Goodbye!")
    exit()
