# lib/helpers.py
from models.owner import Owner

def helper_1():
    print("Performing useful function#1.")


##Owner Class
    
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




## Museum Class
        
def get_all_museum():
    museums = Museum.get_all()
    for museum in museums:
        print(museum)

def create_new_museum():
    name = input("Enter the museum's name: ")
    try:
        museum = Museum.create(name)
        print(f'Success: {museum}')
    except Exception as exc:
        print("Error creating museum: ", exc)

## Exhibition Class
        
def get_all_exhibition():
    exhibition = Exhibition.get_all()
    for exhibition in exhibition:
        print(exhibition)

def create_exhibition(): 
    exhibition = input("Enter the exhibition's name: ")
    try:
        exhibition = Exhibition.create(exhibition)
        print(f'Success: {exhibition}')
    except Exception as exc:
        print("Error creating exhibition: ", exc)

def get_exhibition_by_name():
    name = input("Which exhibition do you want to look at?")
    if isinstance(name, str):
        try: 
            exhibition = Exhibition.get_by_name(name)
            print(f'Success: {exhibition}')
        except Exception as exc:
            print("Error finding exhibition: ", exc)
    else: 
        raise TypeError("please choose an string")
    
# def get_all_art(exhibition_id):
#     if isinstance(exhibition_id, int):
#         try: 
#             art_list = Exhibition.get_all_art(id)
#             for art in art_list:
#                 print(art)
#         except Exception as exc:
#             print("Error finding artworks: ", exc)
#     else: 
#         raise TypeError("please choose an integer")

# def get_all_requests(exhibition_id):
#     if isinstance(exhibition_id, int):
#         try: 
#             request_list = Exhibition.get_all_requests(id)
#             for request in request_list:
#                 print(request)
#         except Exception as exc:
#             print("Error finding loan requests: ", exc)
#     else: 
#         raise TypeError("please choose an integer")

def exit_program():
    print("Goodbye!")
    exit()
