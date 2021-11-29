vowels = 'aeiou'
user_input = input("Enter a string: ")
string = user_input.casefold()
count_vowels = {}.fromkeys(vowels, 0)
for x in string:
    if x in count_vowels:
        count_vowels[x] += 1

print("Total number of vowels - ", count_vowels)