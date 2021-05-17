
# Import Statements
import mysql.connector
from mysql.connector import errorcode


#Database Config
config = {
    "user": "whatabook_user",
    'password': "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True

}

""" FUNCTIONS """


def show_menu():
    print("*" * 30)
    print("\t MAIN MENU")
    print("*" * 30)

    print("""
        1. View Books

        2. Store Locations

        3. My Account

        4. Exit
    """)

    try:
        user_input = int(input("Please choose a menu option: "))

        return user_input

    except ValueError:
        print("That number is not recognized. Please try again...")
        quit()


def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")

    books = _cursor.fetchall()

    print("*" * 30)
    print("\t BOOK LISTING")
    print("*" * 30)

    for book in books:
        print(f" Book ID: {book[0]}\n Book Name: {book[1]}\n Book Author: {book[2]}\n Details: {book[3]}\n")


def show_location(_cursor):
    _cursor.execute("SELECT store_id, locale FROM store")

    locations = _cursor.fetchall()

    print("*" * 30)
    print("\t LOCATIONS")
    print("*" * 30)

    for location in locations:
        print(f" Location: {location[1]}")


def validate_user():
    try:
        user_id = int(input(" Please enter your user id: "))

        if user_id < 0 or user_id > 3:
            print("Incorrect user id. Please try again...")
            quit()
        return user_id
    except ValueError:
        print("You have enterd an incorrect value. Please try again...")


def show_account_menu():

    print("*" * 30)
    print("\t ACCOUNT MENU")
    print("*" * 30)

    print("""
        1. Add Book

        2. Wishlist

        3. Back to main menu

        """)

    try:
        user_input = int(input(" Please select a menu option: "))
        return user_input

    except ValueError:
        print("\n You have enterd an incorrect value. PLease try again...")
        quit()


def show_wishlist(_cursor, _user_id):
    _cursor.execute(f"SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book on wishlist.book_id = book.book_id WHERE user.user_id = {_user_id}")

    wishlists = _cursor.fetchall()

    print("*" * 30)
    print("\t WISHLIST")
    print("*" * 30)

    for wishlist in wishlists:
        print(f" Book Name: {wishlist[4]}\n Author: {wishlist[5]}\n\n")


def show_books_to_add(_cursor, _user_id):
    _cursor.execute(f"SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {_user_id})")

    books_to_add = _cursor.fetchall()

    print("*" * 30)
    print("\t BOOKS TO ADD")
    print("*" * 30)

    for book in books_to_add:
        print(f" Book ID: {book[0]}\n Book Name: {book[1]}\n ")


def add_book_to_wishlist(_cursor, _user_id, _book_id):
   _cursor.execute(f"INSERT INTO wishlist(user_id, book_id) VALUES({_user_id},{_book_id})")
    
try:

    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("*" * 30)
    print("     WELCOME TO WHATABOOK")
    print("*" * 30)

    #Shows the menu 
    user_menu_choice = None
    
    while user_menu_choice != 4:
        user_menu_choice = show_menu()
        
        if user_menu_choice < 0 or user_menu_choice > 4:
            print("\nYou have entered an incorrect value. Please try again....\n\n")

        if user_menu_choice == 1:
            show_books(cursor)

        
        if user_menu_choice == 2:
            show_location(cursor)
            continue

        if user_menu_choice == 3:
            user_id = validate_user()
            account_menu = show_account_menu()

            while account_menu !=3:
                
                
                if account_menu < 0 or account_menu > 3:
                    print("\nYou have entered an incorrect value. Please try again...")
                    
                if account_menu == 1:
                    show_books_to_add(cursor, user_id)
                    
                    book_id =int(input("\n Please enter the ID of the book you want to add: "))

                    add_book_to_wishlist(cursor, user_id, book_id)

                    db.commit()

                    print("The book has been added to the wishlist")

                if account_menu == 2:
                    show_wishlist(cursor, user_id)
                account_menu = show_account_menu()
            print("Back to Main Menu...")

            
    print("Thank you come again... You have now exited the program...")
        

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The password was incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The database speficied does not exist")
    else:
        print(err)

finally:
    db.close()
