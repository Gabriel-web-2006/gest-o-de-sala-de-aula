import sqlite3

banco = sqlite3.connect('primeiro_banco.db') #inserindo intens no banco

cursor  = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text,idade integer, email text)")

cursor.execute("INSERT INTO pessoas VALUES('helena',17,'meia22@gmail.com')")

banco.commit()

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())