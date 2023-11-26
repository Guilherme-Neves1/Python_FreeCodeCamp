# Dictionaries
print("")
band = {
  "vocals": "Plant",
  "guitar": "Page"
}

band2 = dict(vocals="Palnt", guitar="Page")
print("")

print(band)
print(band2)

print(type(band))
print(len(band))

print(type(band2))
print(len(band2))

# Acces items
print("")

print(band["vocals"])
print(band.get("guitar"))

# List all keys
print("")

print(band.keys())

# Lisat all values
print(band.values())

# List of key/value pairs as tuples
print(band.items())

print("")
# Verify a key exists
print("guitar" in band)
print("triangle" in band)

print("")
# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

print("")
# Remove items
print(band.pop("bass"))
print(band)

print("")
band["drums"] = "Bonham"
print(band)

print("")
print(band.popitem()) # tuple
print(band)

print("")
# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band) 

band2.clear()
print(band2)

del band2

print("")
# Copy dictionaries

## BAD COPY!
# band2 = band # create a reference
# print(band2)
# print(band) 

# band2["drums"] = "Dave"
# print(band)

## GOOD COPY!
band2 = band.copy()
band2["drums"] = "Dave"

print(band)
print(band2)

# Or use the dict() constructor function
## GOOD COPY!
band3 = dict(band)
print(band3)

# Nested dictionaries

member1 = {
  "name": "Plant",
  "instrument": "vocals"
}

member2  = {
  "name": "Page",
  "instrument": "guitar"
}

band = {
  "member1": member1, 
  "member2": member2
}
print(band)
print(band["member1"]["name"])


