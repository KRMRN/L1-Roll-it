first =  "apple"
second = "banana"

# print them out
print(f"first {first} | second: {second}")

# now switch
first, second = second, first

print("i've swithced things around...")
print(f"first: {first} | second {second}")