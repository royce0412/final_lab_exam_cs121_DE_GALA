import os
from user_manager import UserManager
def Cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
        print("Welcome to Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        try:
            main_choice = input("Enter: ")
            if main_choice == "1":
                pass
            elif main_choice == "2":
                pass
            elif main_choice == "3":
                exit()
            else:
                raise Exception("Invalid choice. Please try again.")

        except Exception as e:
            print("Error: ", e)
            input("Enter to continue...")
            Cls()
            main()

            

