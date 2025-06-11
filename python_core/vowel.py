str = input("Enter a string: ")
vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0

for char in str:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():  
        consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
