# save url.json into folder first
from json import loads
with open("data.jason","r") as file:
    data = loads(file.read())
print(type(data))

# Microsoft edge tool
# have 2 window , one is the browser and another is the developer tools of the browser
# in the developer tools, there are many tabs like console, network, performance etc.
# we can use these tools to monitor what happens when we do something on the website
