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
    update_exhibition_status
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


def cli_1_print():
    print("Please select an option:")
    print("1. Owners")
    print("2. Museums")

def cli_1_function(): 
    while True:
        cli_1_print()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            owner_menu()
            # break
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
        cli()
        choice = input("> ")

        if choice == "0":
            main_menu()
            break
        elif choice == "1":       
            cli_3_owner_existing_function()
            break

        elif choice == "2":
            create_owner()
            select_existing_owner()
        else:
            print("Invalid choice")

def cli_3_owner_existing_print():
    print("0. Back to main menu")
    print("1. Manage artworks")
    print("2. View loan requests")
    print("3. View exhibitions")

def cli_3_existing_function(): 
    pass

def cli_3_create_new_print():
    pass

def cli_3_create_new_function(): 
    pass

def cli_4_owner_print():
    pass 

def cli_4_owner_function(): 
    pass

def cli_4_museum_print():
    pass

def cli_4_museum_function(): 
    pass

def cli_5_owner_exhibitions_print():
    pass

def cli_5_owner_exhibitions_function(): 
    pass

def cli_5_owner_art_print():
    pass

def cli_5_owner_art_function(): 
    pass

def cli_5_museum_exhibition_list_print():
    pass

def cli_5_museum_exhibition_list_function(): 
    pass

def cli_5_museum_create_exhib_print():
    pass

def cli_5_museum_create_exhib_function(): 
    pass

def cli_6_owner_request_print():
    pass 

def cli_6_owner_request_function(): 
    pass

def cli_6_owner_new_art_print():
    pass

def cli_6_owner_new_art_function(): 
    pass

def cli_6_museum_manage_exhib_print():
    pass

def cli_6_museum_manage_exhib_function(): 
    pass

def cli_7_museum_new_request():
    pass 

def cli_7_museum_new_request():
    pass 

def cli_7_museum_list_requests():
    pass 

def cli_7_museum_list_requests():
    pass 
