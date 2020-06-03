# author- samuel - UI design initially concepted by sammie~
#this section of the code functions as the Main() essentially... and functions as the gathering house of all the code

# ----------------------------------------------------------------------
# Import Section
# ----------------------------------------------------------------------

import sys #typically used for the SYS.exit() commands, but may be used for other purposes
import API
import database


API_CONNECTION = API.API_CONNECTOR("sk_f79736950491411c9a02a29d27108aa0","pk_dc0f023c3e8a445c96dd513c6f795060", "https://cloud.iexapis.com/stable/")


# ----------------------------------------------------------------------
# Var Section
# ----------------------------------------------------------------------

data_list = database.data_store()
# the initilasation of any needed vars for this section of the application

displayVer = 1  # VAR to track need to display a runtime Ver/App Name Message (located in the While Main)
displayVer = int(displayVer)	#used to keep correct VARTYPE
program_Version = 0.5  # VAR used to notate the version number of the UI application feature (Programmer entered value)
choice = 10  # VAR used to decide user input during primary while loop (NOTE) "setup using '10' to avoid any unesssary program exits due to user error
choice = int(choice)	#used to keep correct VARTYPE
stringSearch = "Default"  # VAR used to decide what the user wishes to search up whilst referencing the online API-repository
stockSave = "Default"  # VAR used to decide what stock to download and save from the online API-repository and save locally in the dictonary system
deleteRequest = "Default"  # VAR used to decide what stock to delete from the local dictonary system
sample = "WMT"  # Tester Var "Walmarts" Stock name to be used in any required tests during Development or Based on any need during runtime
areYouSure = 3	#VAR designed to be used during are you sure checks
areYouSure = int(areYouSure)	#Just to make sure it remains an int 


# ----------------------------------------------------------------------
# Main Runtime Section
# ----------------------------------------------------------------------


while choice != 0:		#Begin of the main WHILE loop, that serves as the core functionality for most of the program

	if displayVer > 0:
		print ("  _____ _______      _______ _____  ______ _   _ _____    _______ _____            _____ _  ________ _____  ")
		print (" |  __ \_   _\ \    / /_   _|  __ \|  ____| \ | |  __ \  |__   __|  __ \     /\   / ____| |/ /  ____|  __ \ ")
		print (" | |  | || |  \ \  / /  | | | |  | | |__  |  \| | |  | |    | |  | |__) |   /  \ | |    | ' /| |__  | |__) |")
		print (" | |  | || |   \ \/ /   | | | |  | |  __| |  \` | |  | |    | |  |  _  /   / /\ \| |    |  < |  __| |  _  /")
		print (" | |__| || |_   \  /   _| |_| |__| | |____| |\  | |__| |    | |  | | \ \  / ____ \ |____| . \| |____| | \ \ ")
		print (" |_____/_____|   \/   |_____|_____/|______|_| \_|_____/     |_|  |_|  \_\/_/    \_\_____|_|\_\______|_|  \_\"")
		print ("                                                                                                            ")
		print ("                                                                                                            ")
		print("You are using the Dividend Tracker Application ", program_Version, "\n")
		print ("____________________________________________________________________________________________________________\n\n")
	else:
		displayVer += 1		#designed as a ghost feature, displays the version less obtrusivley as the initial message, after one iteration of the basic while loop
	# start the user introductions and basic summary of the programs purpose for ease of use
	print("Welcome to the Dividend Tracker Application ", program_Version," , UN-Copyrighted version")
	print("the purpose of this application is to aid in the searching and tracking of stocks using Dividends")

	print("[0] to end the program and cease execution")  # User choice to end execution of application
	print("[1] See your Stock Dividend Watchlist")  # User choice to search exsiting entries of the application, and display them upon command
	print("[2] Search a online stock and display some information about it")  # User choice to search the online API-repository and display requested results and their relevant information to the user
	print("[3] Dividend Tracker")  # User choice to add a specific stock to the internal dictionary from the online API-repository
	print("[4] to remove a stock from your Watchlist")  # User choice to remove a specific stock from the internal dictionary
	
	choice = input("\nPlease make your decision (please only 0-4 otherwise the program will ignore your input)")
	choice = int(choice)	#used to keep correct VARTYPE
	

	if choice == 0:
		print("\n\nAre you sure you want to end the application?")  # User choice to end execution of application
		
		areYouSure = input("Enter 0 to Cancel, Enter 1 if you are sure you would like to exit the program")	#just a Verifyer just in case an accedental keypress led user to this option
		areYouSure = int(areYouSure)	#Just to make sure it remains an int (Just a Redundant peice of code JIC)
		
		if areYouSure == 0:		#If selected designed to return user to program
			choice = 10
			choice = int(choice)
			print("returning to program")
			
		elif areYouSure == 1:	#if chosen designed to exit with no trouble
			print("Closing program")
			
		else:	#if any errors occur during input designed to return to program
			print("Invalid Input Entered returning to program")
			choice = 10
			choice = int(choice)

	elif choice == 1:
		print("\n1 entered, loading internal database for you to view")  # User choice to search exsiting entries of the application, and display them upon command
		print("You Currently have these Stocks in your Watchlist")
		for key in data_list:
			print(key)
			
		


	elif choice == 2:
		print("\n2 entered, preparing to search online market, please input a stock you would like to search")  # User choice to search the online API-repository and display requested results and their relevant information to the user
		i_user_input_stock = input("Enter a Stock symbol to check or [!] to exit >>").upper()
		while i_user_input_stock not in ["!"]:
			database2 = database.Database(i_user_input_stock)
			i_user_input_stock = input("Enter Another Stock to check or [!] to exit >>").upper()
			data_input_print = database2.export_quote()
			print(data_input_print)

		print("Back to menu")

	elif choice == 3:
		print("\n3 entered, loading online database, please input a stock you would like to save")  # User choice to add a specific stock to the internal dictionary from the online API-repository
		print("You currently have these stocks in your watchlist,")
		for key in data_list:
			print(key)


		i_user_input = input("Would you like to enter a stock to your watch List? [Y] or [N] >>").upper()

		while i_user_input not in ["Y", "N"]:
			i_user_input = input("Would you like to enter a stock to your watch List? **MUST ENTER** [Y] or [N] >>").upper()

		if i_user_input == "Y":
			i_user_input_stock = input("Enter The Stock Symbol to add or [!] to exit >>").upper()
			while i_user_input_stock not in ["!"]:
				database2 = database.Database(i_user_input_stock)
				data_input_print = database2.export()
				print (data_input_print)
				i_user_input_stock = input("Enter Another Stock to add or [!] to exit >>").upper()
		
		if i_user_input == "N":
			
			print("Returning to program")
			

			for d in database.return_dividends():
				for key in d:
					print ("\n\n Symbol",key)
					if type(d[key]) is list:
						for dd in d[key]:
							for kk in dd:
								if kk == "description":
									print("%s: %s" % (kk, dd[kk]))
								if kk == "exDate":
									print("%s: %s" % (kk, dd[kk]))
								if kk == "recordDate":
									print("%s: %s" % (kk, dd[kk]))
								if kk == "paymentDate":
									print("%s: %s" % (kk, dd[kk]))

	elif choice == 4:
		print("\n4 entered,  loading internal database, please veiw the list and input a stock you would like to remove")  # User choice to remove a specific stock from the internal dictionary
		i_user_input_stock = input("Enter The Stock Symbol to remove or [!] to exit >>").upper()
		while i_user_input_stock not in ["!"]:

			data_input_print = database.delete(i_user_input_stock)
			print ("Removing", i_user_input_stock)
			i_user_input_stock = input("Enter Another Stock to remove or [!] to exit >>").upper()
		

	elif choice == 69:	#easter egg code
		print("You are NOT supposed to enter that filthy number!!! act civil and use this program right!!")

	else:
		print("\nyou have entered an invalid or unrecognized input please try agian")

		choice = 10  # This is a command to keep the choice from glitching out at any point, upon no user input this keeps the choice always at a default so it doesnt loop a statement if no user input occurs

	input("Press Enter to continue...")
	print("\n\n")
	
sys.exit('Program Has Exited, Have a Lovley Day')	#End Of Execution Script



# END OF CODE
