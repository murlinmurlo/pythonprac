input_string = input()
words = input_string.split()

if words[0] == input_string and "yes" in input_string:
    print("yes")
if words[1] == input_string:
    print("second")
if words[2] == input_string and input_string.endswith(words[1]):
    print("third")
