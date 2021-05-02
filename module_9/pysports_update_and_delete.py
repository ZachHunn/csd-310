"""
Zachary Hunn
04/30/2021
Assignment 9.3
"""

# Import Statements
import mysql.connector
from mysql.connector import errorcode

#Database Config
config = {
    "user": "pysports_user",
    'password': "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True

}


#Connect to the database

try:

    db = mysql.connector.connect(**config)

    print(f"\nDatabse user {config['user']} conntected to MySQL on host {config['host']} with database {config['database']}\n")

    cursor = db.cursor()

    #Insert into database
    sql_cmd = "INSERT INTO player(first_name, last_name, team_id) VALUES(%s, %s, %s)"
    sql_val = ('Smeagol', 'Shire Folk', 1)
    cursor.execute(sql_cmd, sql_val)
    db.commit()

    #View players/Inner Join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team on player.team_id = team.team_id ")

    players = cursor.fetchall()

    
    print("------- DISPLAYING PLAYERS AFTER INSERT-------")
    for player in players:
        print(f" Player ID: {player[0]} \n First Name: {player[1]} \n Last Name: {player[2]} \n Team Name: {player[3]}\n")


    #Update
    cursor.execute("UPDATE player set team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol' ")
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team on player.team_id = team.team_id ")
    players = cursor.fetchall()
    print("------- DISPLAYING PLAYERS AFTER UPDATE-------")
    for player in players:
        print(f" Player ID: {player[0]} \n First Name: {player[1]} \n Last Name: {player[2]} \n Team Name: {player[3]}\n")
    



    #Delete
    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum' ")
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team on player.team_id = team.team_id ")
    players = cursor.fetchall()
    print("------- DISPLAYING PLAYERS AFTER DELETE-------")
    for player in players:
        print(f" Player ID: {player[0]} \n First Name: {player[1]} \n Last Name: {player[2]} \n Team Name: {player[3]}\n")



except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The password was incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The database speficied does not exist")
    else:
        print(err)

finally:
    db.close()
