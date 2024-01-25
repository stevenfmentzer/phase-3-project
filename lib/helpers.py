# lib/helpers.py
from models.owner import Owner
from models.museum import Museum
from models.exhibition import Exhibition
from models.art import Art
from models.request import Request
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

def delete_art():
    id = input("Enter the art's id: ")
    if art := Art.find_by_id(id):
        art.delete()
        print(f'Art {id} deleted!')
    else:
        print(f'Art {id} not found')

## Art Class
        
def get_all_art():
    return Art.get_all()

## Museum Class
        
def get_all_museum():       
    museum_names = []
    count = 1
    museums = Museum.get_all()
    for museum in museums:
        if museum.name not in museum_names:
            museum_names.append(museum.name)
            print(f"{count}: {museum.name}")
            count += 1
    return museum_names


def create_new_museum():
    name = input("Enter the museum's name: ")
    try:
        museum = Museum.create(name)
        print(f'Success: {museum}')
    except Exception as exc:
        print("Error creating museum: ", exc)

## Exhibition Class
        
def get_all_exhibition():
    exhibition_names = []
    count = 1
    exhibitions = Exhibition.get_all()
    for exhibition in exhibitions:
        if exhibition.name not in exhibition_names:
            exhibition_names.append(exhibition.name)
            print(f"{count}: {exhibition.name}")
            count += 1
    return exhibition_names

def create_exhibition(museum_name): 
    # Get input for exhibition details
    museum_list =  Museum.get_by_name(museum_name)
    name = input("Enter the exhibition's name: ")
    print("Enter the ID of selected artwork: ")
    arts = Art.get_all()
    count = 1
    for art in arts: 
        print(f"{count}: {art.name}")
        count += 1
    art_id = int(input("> "))
    museum_id = museum_list[0].id
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Create the exhibition with the provided details
    try:
        exhibition = Exhibition.create(name, art_id, museum_id, start_date, end_date)
        print(f'Success: {exhibition}')
    except Exception as exc:
        print("Error creating exhibition: ", exc)

def get_exhibition_by_name():
    print("hello")
    name = input("Which exhibition do you want to look at? ")
    print(name)
    if isinstance(name, str):
        print(f"{name}: has been checked and is a 'string'")
        try: 
            print("trying")
            exhibitions = Exhibition.get_by_name(name)
            print(exhibitions)
            if exhibitions:
                print(f'Exhibition Name: {exhibitions[0].name}')
                print(f'Museum ID: {exhibitions[0].museum_id}')
                print(f'Start Date: {exhibitions[0].start_date}')
                print(f'End Date: {exhibitions[0].end_date}')
            
                for exhibition in exhibitions:
                    print(f'Art ID: {exhibition.art_id}')
            else:
                print(f'No exhibition found with the name: {name}')
        except Exception as exc:
            print("Error finding exhibition: ", exc)
    else: 
        raise TypeError("Please choose a string")
    
def update_exhibition_name():
    name = input("Which exhibition do you want to update? ")
    try:
        exhibitions = Exhibition.get_by_name(name)
        if exhibitions:
            print(f'Exhibitions found with the name: {name}')

            new_name = input("Enter the new name for the exhibition: ")

            for exhibition in exhibitions:
                exhibition.name = new_name
                exhibition.update_by_name()

            print(f'Exhibition Name updated to: {new_name} for all matching instances')
        else:
            print(f'No exhibition found with the name: {name}')
    except Exception as exc:
        print("Error updating exhibition name: ", exc)

def update_exhibition_dates():
    pass

def update_exhibition_status():
    pass
    
## Request Class

def get_all_request():
    requests = Request.get_all()
    for request in requests:
        print(request)

def create_request(exhibition_name, art_id):
    # create(cls, art_id, owner_id, exebition_id, approved)
    owner_id = Art.find_by_id(art_id).owner_id
    Request.create(art_id, owner_id, exhibition_name, False)
    print("")
    print(f"You successfully requested '{Art.find_by_id(art_id).name}' from {Owner.find_by_id(owner_id).name}!")
    print("")

def get_requests_by_exhibition_name(exhibition_name):
    exhibition = Exhibition.get_by_name(exhibition_name)
    museum = Exhibition.get_by_museum_id(exhibition[0].museum_id)[0].id
    requests = Request.find_by_museum_id(museum)
    return requests


def exit_program():
    print("Goodbye!")
    exit()

# ipdb.set_trace()
