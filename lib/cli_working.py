# lib/cli.py

from helpers import (
    exit_program,
    list_owners,
    create_owner,
    get_owner_name_by_id,
    list_owner_arts, 
    add_new_art,
    get_exhibition_by_name,
    create_exhibition, 
    get_all_exhibition, 
    update_exhibition_name, 
    update_exhibition_dates, 
    update_exhibition_status,
    get_all_museum,
    create_new_museum,
    get_all_request, 
    create_request, 
    get_all_art
)

# list structure:
# print("Please select an option:")
# print("1. Owners")
# print("2. Museums")
# print("3. By Exhibition by name")
# print("4: Create Exhibit")
# print("5: Get all Exhibits")
# print("6: Update an Exhibition")
# print("0. Exit the program")


selected_exhibition = None
selected_museum = None


def cli_1_print():
    print("Please select an option:")
    print("0. Exit program")
    print("1. Owners")
    print("2. Museums")

def cli_1_function(): 
    while True:
        cli_1_print()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            cli_2_owner_function()
            # break
        elif choice == "2":
            cli_2_museum_function()
        else:
            print("Invalid choice")

def cli_2_owner_print():
    print("Owner, Please selecte an option:")
    print("0. Back to main menu")
    print("1. existing owner")
    print("2. create new owner")

def cli_2_owner_function(): 
    print("Welcome, Owner!")
    while True:
        cli_2_owner_print()
        choice = input("> ")

        if choice == "0":
            # cli_1_print()
            break
        elif choice == "1":       
            # cli_3_owner_existing_function()
            cli_3_existing_owner_print()
            break

        elif choice == "2":
            create_owner()
            cli_3_existing_owner_print()
        else:
            print("Invalid choice")

def cli_2_museum_print():
    print("Museum, Please selecte an option:")
    print("0. Back to main menu")
    print("1. existing museum")
    print("2. create new museum")

def cli_2_museum_function():
    print("Welcome, Museum!")
    while True:
        cli_2_museum_print()
        choice = input("> ")

        if choice == "0":
            # cli_1_print()
            break
        elif choice == "1":       
            cli_3_existing_museum_print()
            break

        elif choice == "2":
            create_new_museum()
            cli_3_existing_museum_print()

        else:
            print("Invalid choice")

def cli_3_existing_museum_print():
    print("Welcome Museum! Select an existing museum:")
    get_all_museum()
    

def cli_3_existing_owner_print():
    print("Welcome Owner! Select an existing owner:")  # can delete as input is shown below
    list_owners()

    owner_id = input("Enter the ID of the owner you want to choose: ")
    owner_name = get_owner_name_by_id(owner_id)
    cli_4_existing_owner_function(owner_name, owner_id)


def cli_4_existing_owner_print():
    print("0. Back to previous menu")
    print("1. Manage artworks")
    print("2. View loan requests")
    print("3. View exhibitions")

def cli_4_existing_owner_function(owner_name, owner_id):
    print(f"Welcome, {owner_name}! What would you like to do?")
    while True:
        cli_4_existing_owner_print()
        choice = input("> ")

        if choice == "0":
            cli_3_existing_owner_print()
            break
        elif choice == "1":
            cli_5_owner_print(owner_id)
            break

        elif choice == "2":
            # view_loan_requests()
            get_all_request()
            pass
        elif choice == "3":
            get_all_exhibition()
            pass
        else:
            print("Invalid choice")

def cli_5_owner_print(owner_id):
    from models.owner import Owner
    owner = Owner.find_by_id(owner_id)
    owner_name = owner.name

    print("0. Back to main menu")
    print("1. View all arts")
    print("2. Add new art")
    print("3. delete art")
    

def cli_3_existing_function(): 
    pass

def cli_3_create_new_print():
    pass

def cli_3_create_new_function(): 
    pass

###IGOR START HERE
def cli_5_owner_request_print():
    pass 

def cli_5_owner_requests_function(): 
    pass

def cli_4_museum_print():
    print("What would you like to do?")
    print("1: View all exhibitions")
    print("2: Start a new exhibition")
    print("0: exit")

def cli_4_museum_function(): 
    while True: 
        cli_4_museum_print()
        choice = input("> ")
        # View all exhibitions
        if choice == "1":
            cli_5_museum_exhibition_list_function()
        # Start a new exhibition
        if choice == "2": 
            cli_5_museum_create_exhib_function()
        # BACK
        elif choice == "0":
            cli_3_existing_function  ##### DOUBLE CHECK THE FUNCTION NAME #######
        else: 
            print("invalid choice")

def cli_5_owner_exhibitions_print():
    pass

def cli_5_owner_exhibitions_function(): 
    pass

def cli_5_owner_art_print():
    pass

def cli_5_owner_art_function(): 
    pass

# Not needed
# def cli_5_museum_exhibition_list_print():
#     pass
 
def cli_5_museum_exhibition_list_function():
    print("Which exhibition do you want to manage?")
    exhibition_list = get_all_exhibition() 
    while True: 
        choice = input("> ")
        # If choice is in range of options go to that choice
        if 0 < int(choice) <= len(exhibition_list):
            cli_6_museum_manage_exhib_function(exhibition_list[choice-1])
        # BACK
        elif choice =="0":
            cli_4_museum_function()
        else: 
            print("invalid choice")

def cli_5_museum_create_exhib_print():
    print("What would you like to do?")

def cli_5_museum_create_exhib_function():
    while True: 
        cli_5_museum_create_exhib_print()
        choice = input("> ")
        if choice == "1":
            pass
        if choice == "2": 
            pass
        elif choice == "0":
            break
        else: 
            print("invalid choice")

def cli_6_owner_request_print():
    pass 

def cli_6_owner_request_function(): 
    pass

def cli_6_owner_new_art_print():
    pass

def cli_6_owner_new_art_function(): 
    pass

def cli_6_museum_manage_exhib_print(exhibition_name):
    print("What would you like to do?")
    print(f"1: See all confirmed artworks in {exhibition_name}.")
    print(f"2: Request a new artwork for {exhibition_name}.")
    print("3: View pending loan requests.")
    print("0: back")

def cli_6_museum_manage_exhib_function(exhibition_name): 
    while True: 
        cli_6_museum_manage_exhib_print(exhibition_name)
        choice = input("> ")
        # See all confirmed artworks in {exhibition_name}
        if choice == "1":
            print("Sorry, that feature isn't working yet.")
        # Request a new artwork for {exhibition_name}
        if choice == "2": 
            cli_7_museum_new_request_function(exhibition_name)
        # View pending loan requests
        if choice == "3":
            cli_7_museum_list_requests_function(exhibition_name)
        # BACK
        elif choice == "0":
            cli_5_museum_exhibition_list_function()
        else: 
            print("invalid choice")

def cli_7_museum_new_request_print(arts):
    count = 1
    for art in arts: 
        print(f"{count}: {art.name}")
    print("0: back")

def cli_7_museum_new_request_function(exhibition_name):
    print("What artwork would you like to request?")
    arts = get_all_art()
    cli_7_museum_new_request_function(arts)
    while True:
        choice = input("> ")
        if 0 < int(choice) <= len(arts):
            create_request(exhibition_name, arts[choice-1])
        # BACK
        elif choice == "0":
            cli_6_museum_manage_exhib_function(exhibition_name)
        else: 
            print("invalid choice")


def cli_7_museum_list_requests_print(exhibition_name):
    # LIST ALL REQUESTS
    print("0: back")

def cli_7_museum_list_requests_function():
    pass 

if __name__ == "__main__":
    cli_1_function()