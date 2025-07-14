import json
from pathlib import Path

movies = [
    {"id":1, "ttile": "movie1", "year":100},
    {"id":2, "ttile": "movie2", "year":200},
]

# jsonFile = json.dumps(movies)

# print(jsonFile)
# print(type(jsonFile))

# path = Path("jsonfile.json").write_text(jsonFile)

json_content = Path("jsonfile.json").read_text();

json_content = json.loads(json_content)
print(json_content)
print(json_content[0])
print(json_content[0]["ttile"])
