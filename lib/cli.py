# lib/cli.py


from helpers import (
    exit_program,
    list_owners,
    create_owner
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
            list_owners()
        elif choice == "2":
            create_owner()
        else:
            print("Invalid choice")

def owner_options():
    print("Owner, Please selecte an option:")
    print("0. Back to main menu")
    print("1. existing owner")
    print("2. create new owner")


if __name__ == "__main__":
    main()
