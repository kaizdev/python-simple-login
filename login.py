# Introduction to Programming - Project - Kai Zhang - Creating a SimpleLogin program

# ------ Function libraries used in this program --------
import string # Need this for punctuation and letters
import random # Need this for the random password generation
import time # Need this to delay the exit for 2 seconds

# ------ Define a function that generates the password based on user inputs --------
def generate_password(length, letters, digits, symbols):
    characters = '' # Initialise the string of characters
    if letters:
        characters += string.ascii_letters
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

# ------ Get user input - Are they existing or new user? --------
valid = False
while valid == False:
    print("********** Menu **********")
    print("Type L/l for login")
    print("R/r for new registration")
    print("V/v for viewing (Admin access)")
    print("E/e for exit")
    print("**************************")
    options1 = str(input("Select one of the above options: "))

# -------- Keep asking for input if an invalid selection is selected --------
    if options1 in ['l', 'L', 'r', 'R', 'v', 'V', 'e', 'E']:
        valid = True
    else:
        print("Invalid Option")

# Exit the program if E or e is selected        
if options1 == 'e' or options1 == 'E':
        print('Will exit in 2 seconds')
        n = 2
        while n > 0:
            print(n)
            time.sleep(1) # Adds 1 second delay prior to exiting the program (runs twice)
            n -= 1
        print("Program exited")
        exit()

# -------- Login (L) ---- Prompt for user / password for existing users --------
if options1 == "L" or options1 == 'l':
    valid = False

    while valid == False: #Keep prompting the user for username and password if invalid details are entered
        # Prompt user for password
        invcharacters = list(string.punctuation) # Included data structure in the creation of the login process
        while True:
            username = input('Please type in your username: ')
            if any((c in invcharacters) for c in username): #this checks for any special characters present in the username
                print("The username can not contain any special character")
            else:
                break

        # Prompt user for their password
        while True:
            password = str(input("Type in your password: "))
            if password == "":
                print("Password required - cannot be blank")
            else:
                break

        # -------- Check the accounts file to validate if the user exists --------
        p = open("accounts.txt", 'r') #read only with r
        found = False
        for x in p:
            list_un_pw = x.split(" ")
            list_un_pw[0] = list_un_pw[0].rstrip("\n")
            list_un_pw[1] = list_un_pw[1].rstrip("\n")
            if list_un_pw[0] == username and list_un_pw[1] == password:
                found = True
                break
        if found == True:
            print("Valid User")
            valid = True #break out of the while loop if correct details are entered
        else:
            print("Invalid User")

# -------- Register (R)--------

# print(f'User name entered as {username} and password entered as {password}')

if options1 == 'r' or options1 == 'R':
    print("OK let's try a new registration")
    username = input("Type in your username: ") # <--- We should also add in a check to see if special characters here for new registration
    password_option = input("Select own password ('Own') or Generate one for you ('Gen'): ")
    if password_option.lower() == 'own':
        password = input("Type in your password: ") #give option for self password or generated
        # Should also check that the password is not blank (similar)
    else:
        # If user wishes to have a password generated, then collect the desired parameters / arguments from the user
        
        #Length must be an integer - will loop until an integer is given
        while True:
            try:
                length = int(input("Enter desired password length, or select 8 for default password length: "))
                break
            except:
                print("Please enter a valid password length in numbers")
        letters = input("Include letters? (y/n): ").lower() == 'y'
        digits = input("Include digits? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'
        password = generate_password(length, letters, digits, symbols)
        print(f"Your random password is: {password} - Please save this for future reference")
    print("Username and password will now be saved to the accounts file ")

# Usernames and passwords to be saved in accounts.txt upon new registration
    f = open("accounts.txt", "a") #append the username and password to the existing accounts list
    new_line = '\n' #newline is added to the write function to make sure 
    f.write(f'{username} {password}{new_line}')
    f.close() # close the file

# View File (V) -- update this to check for valid username and password
if options1 == 'v' or options1 == 'V':
    print("View file - Admin access only")
    username = input("Type in the admin username: ")
    password = input("Type in the admin password: ")
    if username == 'admin' and password == 'Gel0s23':  # This is the admin user and password saved into the accounts file, for the purpose of this task
        print("Valid User, now printing account details")
        p = open("accounts.txt", 'r')
        for x in p:
            print(x)
    else:
        print("Invalid user")
