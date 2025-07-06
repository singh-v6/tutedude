a = {'Alice': 50, 'John': 63, 'Ram': 98}

inp = input("Enter the student's name: ")

b = a.get(inp)

if b is not None:
    print("{}'s marks: {}".format(inp, b))
else:
    print("Student not found.")
