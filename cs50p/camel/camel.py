variable = input("camelCase: ")
new_variable = ""
for c in variable:
    if(c.isupper()):
        print("_", c.lower(), end="", sep="")
    else:
        print(c, end="")
print()