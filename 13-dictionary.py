# built 
#var = {"key1" : "value1","key2" : "value2"}
#** key and value 
d= {
    "cat" : "เเมว",
    "rat" : 3,
    "bat" : "เเมว",
}

#call with 'Key'
print(d["cat"])
print(d["rat"])
print(d["bat"])

#add new key and value to dictionary
d["horse"] = 5
print(d)

# change value
d["horse"] = 12
print(d)

#delete
del d["horse"]
print(d)

d.keys()
d.values()

for k,v in d.items():
    print(k,v)

d.get("crab",0)