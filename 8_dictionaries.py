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
