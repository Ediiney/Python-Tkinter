import sqlite3 

conn = sqlite3.connect('UsersData.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS User (
  Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  Name TEXT NOT NULL ,
  Email NOT NULL,
  User TEXT NOT NULL,
  Password TEXT NOT NULL   
);
""")

print("Conectado ao Banco de Dados ►")


