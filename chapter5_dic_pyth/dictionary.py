a={
    "fast": "it tell that somethink is quick",
    "believe": "it says that believe in somethink",
    "marks":" it tell some numbers ",
     "score": [4,6,9,43],
     1: 43
}
print(a["fast"])
a["fast"]="she is beautiful"
print(a["fast"])

# method of dictionary
print(a.keys())
# its type is my default is dict_keys but we can convert it into list
print(type(a.keys()))
# convert it into list
print(list(a.keys()))
# print its value
print(a.values())
# it will print set of data
print(a.items())

# to add more keys to a
b={
    "lovish":"friends",
    "love":"pyar"
}
a.update(b)
print(b)

