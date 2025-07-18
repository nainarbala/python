import json
from pathlib import Path
import sqlite3

movies = json.loads(Path("jsonfile.json").read_text())
print(movies)
print(type(movies))

# with sqlite3.connect("db.sqlite3") as conn:
#     commands = "INSERT INTO MOVIE VALUES(?, ?,?)"
#     for movie in movies:
#         conn.execute(commands, tuple(movie.values()))
#     conn.commit()


with sqlite3.connect("db.sqlite3") as conn:
    command = "select * from movie"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)
    
