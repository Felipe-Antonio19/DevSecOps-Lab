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

# cursor.execute("DROP TABLE tasks")

cursor.execute("CREATE TABLE IF NOT EXISTS tasks" \
"(id INTEGER PRIMARY KEY AUTOINCREMENT, " \
"title TEXT NOT NULL, " \
"description TEXT NOT NULL," \
"owner_id INTEGER NOT NULL," \
"FOREIGN KEY(owner_id) REFERENCES users(id))")

# cursor.execute("DELETE FROM users WHERE id = 4")
usuarios = cursor.execute("SELECT * FROM users").fetchall()
# tasks = cursor.execute("SELECT * FROM tasks").fetchall()

print(usuarios)