"""
    Zachary Hunn
    04/30/2021
    Assignment 9.2

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


# Connect to Database
try:

    db = mysql.connector.connect(**config)

    #Output of the connection status
    print(f"\nDatabse user {config['user']} conntected to MySQL on host {config['host']} with database {config['database']}\n")

    cursor = db.cursor()
    #Inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team on player.team_id = team.team_id ")
    
    players = cursor.fetchall()

    print("------- DISPLAYING PLAYERS -------")
    for player in players:
        print(f" Player ID: {player[0]} \n First Name: {player[1]} \n Last Name: {player[2]} \n Team Name: {player[3]}\n")

    
    print("------ DISPLAYING SELECTED PLAYER FROM WHERE CLAUSE ------")
    cursor.execute("SELECT first_name, last_name FROM player WHERE player_id = 3")
    players = cursor.fetchall()
    for player in players:
        print(f"First Name: {player[0]} \nLast Name: {player[1]} \n ")
    

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The password was incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The database speficied does not exist")
    else:
        print(err)

finally:
    db.close()
