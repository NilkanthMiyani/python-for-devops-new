info = {
    "name":"Nilkanth",
    "age": 30,
    "city": "Surat",
    "company": "Appgambit",
    "married": False,
    "fav": ["cricket", "movies"]
}

print("I live in", info["city"])
print("I love", info.get("fa", "Not found")) # By default if choice 1 not fount

info.update({
    "age": 31,
    "city": "Mumbai",
})

print(info)
print(dir(info))

# iterate a dict

for i in info:
    print(i)  # only key

for key,value in info.items():
    print(key,f':',value)


