# Angel Almanzar- Student ID 00330381
# Professor Penta
# Final Project: User Management System
# Programming for IT- CIS-153-L8
# 12/1/25

" Project Description: This project aims to allow users to create accounts and sign in. "
" The program aims to manage the data within a dictonary, where usernames are keys and encrypted passwords become values. "
" All actions made by the user are logged into a text file named log.txt. "

# Start of code:

import random # imports the random module, to create random numbers for lines. lines like the username.

# File Names:

user_data_file = ("user_data.txt") # This is the text file that stores the usernames and passwords.

log_file = open("log.txt", "a") # This is the text file that will save different action records.


# User Dictonary:

user_data = {} # Creating an empty dictonary to store all the user accounts created.

# forbidden password characters:

forbidden = "!@$:?" # cannot be in any passwords.


# Log Entries[Keys, Separator, Values]:

# Keys: # these are the names that would become the key for the username variable.

# username1 = Angel
# username2 = Michael
# username3 = Jameson

# Values: # strings I came up with for the status variable.

# New User, Idea 1
# New Name, Idea 2
# Unique Name, Idea 3

# test code (below):

# log = open("log.txt", "a") # opens the log file and appends it. append means add a single item to the end of a list or string.
# username = "" # the key is the username.
# status = "New User" # the value is the status.
# log.write(f"{username}:{status})") # writes the username and status into the log file using an f string. (Angel: New User).
# log.close() # closes the file.

# Different Separators:

# colon ":"
# comma ","
# equals "="
# two colons "::"
# greater than and less than <, >.

# Password Encryption: # Code incorporated from Problem Set 5(below).

def encrypted_password (password, forbidden): # defines the test password function and has two parameters.
    for char in forbidden: # Loops through the characters in the forbidden parameter. A parameter is a specific variable that gets passed to functions.
        if char in password: # if the characters in the password are in forbidden.
            return False # Returns false if the password is incorrect or uses forbidden characters.
    return True # Returns True if the password is correct.


def make_secret_password (password): # strings are immutable. defines the password encryption.
    newpassword = password[-1] +password[1:-1] +password[0] # scrambles the letters around for the password.
    newpassword = newpassword.replace ("i", "!")# lowercase "i" os replaced at all instances with the "!" symbol.
    newpassword = newpassword.replace("a", "@") # lowercase "a" is replaced at all instances with the "@" at symbol.
    newpassword = newpassword.replace("S", "$") # uppercase "S" is replaced at all instances with the "$" dollar sign symbol.
    newpassword = newpassword.replace("J", "?") # uppercase "J" is replaced at all instances with the "?" question symbol.

    return newpassword # returns the new ecrypted password back into the code.


# Usernames Functions: (from Problem Set 5, changed to have four random digits instead of 3.)

def user_name(firstname, lastname): # defines the username function and adds the firstname and lastname as two different parameters.
        first_initial = firstname[0].lower() # string indexting 0 is the first letter. Example: "mario" m = 0, a =1, r = 2, i = 3, o = 4.
        # .lower() is a string method that retuns all characters to be lowercase letters.
        last_name_lower = lastname.lower() # makes all the letters in the lastname that was written in lowercase.
        random_num = random.randint(1000,9999) # this line creates a random integer with a range from 1000 to 9999.
        new_username = first_initial + last_name_lower + str(random_num) # concatenate's the lines together to create a new username.
        # concatenate means join, or link together, combine.
        # the line combines the first initial, last name and the number and creates a string out of it.

        return new_username # returns the new username entered by the user.


# Functions to implement into code section(had a very hard time with this portion of the project.):

def load_user_data(): # defines the load user data function.
    global user_data # The user data dictonary is stored in the global space.
    user_data_file = open("user_data.txt", "r") # opens the file in read mode.
    for line in user_data_file: # loops through each line in the file.
         print(line) # prints the line.
         line = line.strip() # removes whitespaces from new lines.
         if line: # makes sure the line is not empty.
            if ":" in line: # checks if colon is in the line.
                colon = line.find(":") # checks for colon in line.
                username = line[:colon] # string slicing for username.
                password = line[colon +1:] # gets everything in the password, after the colon.
                user_data[username] = password # stores the data in the dictionary.
                user_data_file.close() # closes file.
                # return user_data # returns the data. commented out. (###### no return needed as it is global.)


def save_user_data(): # defines the save user data function. (###### loop through dictionary and print to file.)

    global user_data # The user data dictonary is stored in the global space.

    data_file = open("user_data.txt" , "w") # opens the file in write mode and erases what is in the file.

    for username, password in user_data.items(): # loop through all the usernames and passwords.

        data_file.write(f"{username}:{password}\n") # writes a pair to the file with a colon separator.


    data_file.close() # closes the file.

    print("Your user data has been saved sucessfully. ") # prints a message to the user that the data has been saved.



def get_username(): # (#### do this it is wicked easy.) tried my best with doing this function.

    username = input("Enter your username: ").strip() # asks the user to input a unique username, and strips the line.

    return username # returns the created username.



def test_valid_password(password): # defines the test valid password function. (##### then do this because get password can use it.)
    # (not sure if this was done correctly, tried my best.) ##### you already have code that can do this work from a problem set.

    if len(password) < 7: # if the length of the password is greater than 7.(tried to create a common password length.)
        print("The password must have at least 7 characters. ") # prints a message to the user about a password length, how long it should be.
        return False # returns false if the length is incorrect.

    for char in forbidden: # goes through each forbidden character in the line.
        if char in password: # checks for forbidden characters in the line.
            print("The password cannot contain:", char) # the password cannot contain forbidden characters.
        return False # returns false if forbidden characters are used.
    return True # returns true if the password length is correct etc.


def get_password(): # defines the get password function.

    ### enter a password
    ### enter a second time
    ### if they are the same call test_valid_pass. If it is ok return the password.

    password = input("Enter your password: ") # ask the user to enter a password.

    return password # returns the user passsword.


# def update_password(): # defines the update password function.
# asks the user if they would like to update their password(code below).


# def add_user(username, password): # defines the add user function with the username and password as parameters. (###### put a new enty in the dictionary, but where is the dictionary?(global).)
# global user_data # gets the function and updates the user data dictonary within global.


    def check_user(): # defines the check user function.
        if username in user_data: # checks if the username exists as a key in the dictonary.
            encrypted = make_secret_password(password) # encrypts the password and makes it similar to the original input.
        if user_data[username] == encrypted: # compares encrypted passwords, current and saved.
            return True # returns true if the password and username are correct.
    return False # returns false if login is incorrect.

def write_to_log(username, status): # colon can be used for function definitions, loops, and if statements etc.

    log = open("log.txt", "a") # opens the log file.
    log.write(f"{username}:{status})\n") # write to the file.
    log.close() # closes the file.


# test code(below).

# f" f string example
# x = 20 +5
# y = 50
# print(f" This is x: {x}")


# final code section(below):

def display_main_menu(): # defines the main menu function.

# prints the different menu options for the main menu. Tried my best with making the main menu.

    print(f"Welcome to the Main Menu\n")
    print("1. Login\n")
    print("2. Create New User\n")
    print("3. Quit the program?\n")

def display_user_menu(): # defines the user menu function.

    # prints the different menu options for the user menu. Tried my best with making the user menu.

    print(f"Welcome to the User Menu\n")
    print("1. Print Log\n")
    print("2. Update Password?\n")
    print("3. Quit the program?\n")


# original testing code from Problem Set 5, modified(below).

# main code running for program(below).

firstname = input("Enter the firstname:\n") # ask the user to input their firstname.
while ":" in firstname: # checks if a colon is in the firstname.
    print("Incorrect username entered. Cannot contain colons (:).") # prints an error message to the user.
    firstname = input("Enter the firstname:\n") # ask the user to input their firstname.
    # gets a new user name.
lastname = input("Enter the lastname:\n") # ask the user to input their lastname.
while ":" in lastname: # checks if a colon is used within the lastname entered.
    print("Incorrect username entered. Cannot contain colons (:).") # prints an error message to the user.
    lastname = input("Enter the lastname:\n") # ask the user to input their lastname.
username = user_name(firstname,lastname) # creates a new username using the users firstname and lastname, and four random digits.

password = input("Enter your password of choice:\n") # ask the user to input a unique password they can think of.
