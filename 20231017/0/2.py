def count_vowels_consonants(string):
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')
    
    unique_vowels = set()
    unique_consonants = set()
    
    for char in string:
        if char in vowels:
            unique_vowels.add(char)
        elif char in consonants:
            unique_consonants.add(char)
    
    num_vowels = len(unique_vowels)
    num_consonants = len(unique_consonants)
    
    return num_vowels, num_consonants

string = input("Введите строку: ")
print(count_vowels_consonants(string))
