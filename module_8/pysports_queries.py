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
    """ try/catch block for handling potential MySQL database errors """

    db = mysql.connector.connect(**config)  # connect to the pysports database

    cursor = db.cursor()

    
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

 
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")

    
    for team in teams:
        print(f"  Team ID: {team[0]}\n  Team Name: {team[1]}\n  Mascot: {team[2]}\n")

   
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

  
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")

    
    for player in players:
        print(f"  Player ID: {player[0]}\n  First Name: {player[1]}\n  Last Name: {player[2]}\n  Team ID: {player[3]}\n")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
  

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
   

    db.close()
