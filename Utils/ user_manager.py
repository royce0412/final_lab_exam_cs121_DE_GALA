from dice_game import DiceGame
class UserManager:
	User_list = {}

	def load_users():
		pass

	def save_users():
		pass

	def validate_username():
		pass

	def validate_password():
		pass

	def register(self):
		register_username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
		if len(register_username) >= 4:
			register_password = input("Enter username (at least 8 characters), or leave blank to cancel: ")
			if len(register_password) >= 8:
				if username not in User_list:
					User_list[register_username] = User(register_username, register_password)
					
			else:
				input("Username must be at least 8 characters long...Enter to return")
				Cls()
				main()
		else:
			print("Username must be at least 4 characters long.") 

	def login():
		pass