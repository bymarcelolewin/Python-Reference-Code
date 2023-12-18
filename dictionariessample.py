cats = {
    "Jane": 6, 
    "Tom": 14, 
    "Sara": 8
}

print(cats)
print(cats["Tom"])

cats["Wilson"]=2

print(cats)
print(cats["Wilson"])

del(cats["Sara"])

print(cats)
print(cats["Wilson"])

print(f"Dictionary length is {len(cats)}")