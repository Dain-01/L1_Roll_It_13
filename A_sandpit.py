first = "apple"
second = "banana"

#print them out...
print(f"First: {first} | Second {second}")

# now switch them
first, second = second, first

print("ive switched things around...")
print(f"First: {first} | Second {second}")