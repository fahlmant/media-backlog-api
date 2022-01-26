#string Title
#string Studio
#date Release Date
#int Runtime (in minutes)
#string Director
#uuid ID

import json
import uuid
from json import JSONEncoder
from uuid import UUID, uuid1
from webbrowser import get
JSONEncoder_olddefault = JSONEncoder.default
def JSONEncoder_newdefault(self, o):
    if isinstance(o, UUID): return str(o)
    return JSONEncoder_olddefault(self, o)
JSONEncoder.default = JSONEncoder_newdefault


Movies = {
    "Titled": "Spider-Man: No Way Home",
    "Studio": "Columbia Pictures & Marvel Studios",
    "Release Date": int(2021),
    "Runtime": int(148),
    "Director": "Jon Watts",
    "ID": uuid.uuid1()
}

x = json.dumps(Movies, indent = 2)
print(x)

import requests

#GET /<resource>
Titled = Movies.get("Titled")
Studio = Movies.get("Studio")
Release = Movies.get("Release Date")
Runtime = Movies.get("Runtime")
Director = Movies.get("Director")

print(Titled, Studio, Release, Runtime, Director)

#GET /<resource/<uuid>
ID = Movies.get("ID")
print(ID)

#POST /<resource>
Dogs = {"Dogs": "None"}
New = requests.post(Movies, json=Dogs)
print(New)

#PATCH /<resource>/<uuid>
Run = {"Runtime": int(145)}
response = requests.patch(Movies, json=Run)
response.json()

#DELETE /<resource>/<uuid>
response = requests.delete(Movies)
response.json()