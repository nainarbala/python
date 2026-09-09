import json
from pathlib import Path

movies = [{"name": "Terminator"}, {"xxx": "sdg"}, {"sdg": "wet"}]

movies = json.dumps(movies)

Path("movies1.json").write_text(movies)

print(Path("movies1.json").read_text())

data = Path("movies1.json").read_text()
data = json.loads(data)

print(data[0]['name'])
