#!/usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
database="tkinterdb1",
user="root",
password = "root1234"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE etudiant(id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(30),prenom VARCHAR(30),matricule VARCHAR(12),matiere VARCHAR(50),note VARCHAR(10))")
