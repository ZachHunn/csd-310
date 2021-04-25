"""
    Zachary Hunn
    04/25/2021
    Assignment 8.2

    This is to test the python mysql connector
"""

#Imports

import mysql.connector
from mysql.connector import errorcode

#Database config

config = {
    "user": "pysports_user",
    'password': "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True

}


try:
   

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    # output the connection status 
    print(f"\n  Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
 

    db.close()
