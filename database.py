import sqlite3

con = sqlite3.connect("devsecopsDb.db")
cursor = con.cursor()


# User tables
cursor.execute("CREATE TABLE IF NOT EXISTS users"
"(id INTEGER PRIMARY KEY AUTOINCREMENT, " \
"name TEXT NOT NULL, " \
"email TEXT NOT NULL, " \
"senha TEXT NOT NULL, " \
"created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

# cursor.execute("""
#     INSERT INTO users (name, email, senha) VALUES ("Teste", "teste@gmail.com", "123")
# """)

usuarios = cursor.execute("SELECT * FROM users").fetchall()
print(usuarios)