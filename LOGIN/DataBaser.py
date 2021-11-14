import sqlite3 

conn = sqlite3.connect('UsersData.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS User (
  Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  Name TEXT NOT NULL ,
  Email TEXT NOT NULL,
  Users TEXT NOT NULL,
  Pass TEXT NOT NULL   
);
""")

print("Conectado ao Banco de Dados ►")


