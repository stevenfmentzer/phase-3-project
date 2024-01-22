# lib/cli.py


from helpers import (
    exit_program,
    list_owners,
    create_owner,
    get_owner_name_by_id
)


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            owner_menu()
        elif choice == "2":
            pass
        else:
            print("Invalid choice")

            
def main_menu():
    print("Please select an option:")
    print("0. Exit the program")
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
        elif choice == "1":        # no need to show list of owners?
            # list_owners()
            select_existing_owner()

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



def existing_owner_menu(owner_name):
    print(f"Welcome, {owner_name}! What would you like to do?")
    while True:
        existing_owner_options()
        choice = input("> ")

        if choice == "0":
            main_menu()
            break
        elif choice == "1":
            # manage_artworks()
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
    existing_owner_menu(owner_name)






if __name__ == "__main__":
    main()
