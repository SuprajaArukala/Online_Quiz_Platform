import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

questions = [
    ("What is the keyword used to define a function in Python?", "func", "define", "def", "function", "def"),
    ("Which data type is used to store multiple items in a single variable?", "int", "list", "str", "bool", "list"),
    ("Which symbol is used for single-line comments in Python?", "//", "#", "/*", "--", "#"),
    ("Which function is used to display output in Python?", "print()", "echo()", "display()", "show()", "print()"),
    ("Which operator is used for exponentiation in Python?", "^", "**", "*", "//", "**")
]

c.executemany('INSERT INTO questions (question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?)', questions)

conn.commit()
conn.close()
print("Questions added successfully!")
