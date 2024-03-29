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


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            owner_menu()
            # break
        else:
            print("Invalid choice")

            
def main_menu():
    print("Please select an option:")
    print("1. Owners")
    print("2. Museums")
            
def owner_menu():
    print("Welcome, Owner!")
    while True:
        owner_options()
        choice = input("> ")

        if choice == "0":
            main_menu()
            break
        elif choice == "1":       
            select_existing_owner()
            break

            # break
        elif choice == "2":
            create_owner()
            select_existing_owner()
        else:
            print("Invalid choice")

def owner_options():
    print("Owner, Please selecte an option:")
    print("0. Back to main menu")
    print("1. existing owner")
    print("2. create new owner")



def existing_owner_menu(owner_name, owner_id):
    print(f"Welcome, {owner_name}! What would you like to do?")
    while True:
        existing_owner_options()
        choice = input("> ")

        if choice == "0":
            main_menu()
            break
        elif choice == "1":
            manage_art_options(owner_id)
            break

            pass
        elif choice == "2":
            # view_loan_requests()
            pass
        elif choice == "3":
            # view_exhibitions()
            pass
        else:
            print("Invalid choice")
def existing_owner_options():
    print("0. Back to main menu")
    print("1. Manage artworks")
    print("2. View loan requests")
    print("3. View exhibitions")

def select_existing_owner():
    print("Welcome Owner! Select an existing owner:")
    list_owners()
    
    owner_id = input("Enter the ID of the owner you want to choose: ")
    owner_name = get_owner_name_by_id(owner_id)
    existing_owner_menu(owner_name, owner_id)

def manage_art_options(owner_id):
    from models.owner import Owner
    owner = Owner.find_by_id(owner_id)
    owner_name = owner.name


    while True:
        print("0. Back to main menu")
        print("1. View all arts")
        print("2. Add new art")
        print("3. delete art")

        choice = input("> ")

        if choice == "0":
            main_menu()
            break
        elif choice == "1":
            list_owner_arts(owner_id)
        elif choice == "2":
            print(owner.name, owner_id)

            add_new_art(owner_id, owner_name)

            
            
        elif choice == "3":
            # Delete art logic
            pass
        else:
            print("Invalid choice")

def update_exhibition_menu():
    while True:
        update_exhibition_options()
        choice = input("> ")

        if choice == "1":
            update_exhibition_name()
        elif choice == "2":
            update_exhibition_dates()
        elif choice == "3":
            update_exhibition_status()
        else:
            print("Invalid choice")

def update_exhibition_options():
    print("What would you like to update?")
    print("1: Name")
    print("2: Start & End Dates")
    print("3: Update Status")


if __name__ == "__main__":
    main()
