# Dictionaries
band ={
    "vocals": "plant",
    "guitar": "page"
}

band2 = dict(vocals="plant", guitar="page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# List of key/value pairs as tuples
print (band.items())

# verify a key exists
print ("guitar" in band)
print ("triangle" in band)

# change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "bonham" 
print(band)

print(band.popitem()) #tuple
print(band)

# Delete and clear

band["drums"] = "bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries

band2 = band # create a reference
print("bad copy!")
print(band2)
print(band)

band2["drums"] = "Dave"
print(band)
band2 = band.copy()
band2["drums"] ="dave" 
print ("Good copy!")
print(band)
print(band2)


# Nested dictionaries

member1 = { 
    "name": "Page"
    "instrument""gutitar"
}
member2 = { 
    "name": "Page"
    "instrument""gutitar"
}
band = {
    "member1": "member1"
     "member2" "member2"
}
print(band)
print(band["member1"]["name"])

#sets

nums = {1, 2, 3, 4,}

nums2 = set((1, 2, 3, 4,))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))
