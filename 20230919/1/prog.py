num = int(input())
output = ""
if num % 2 == 0 and num % 25 == 0:
    output += "A +"
else:
    output += "A -"

if num % 2 != 0 and num % 25 == 0:
    output += " B +"
else:
    output += " B -"

if num % 8 == 0:
    output += " C +"
else:
    output += " C -"

print(output)
