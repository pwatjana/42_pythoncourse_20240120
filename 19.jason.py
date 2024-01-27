# save url.json into folder first
from json import loads
with open("data.jason","r") as file:
    data = loads(file.read())
print(type(data))