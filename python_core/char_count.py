string = "hello world"
char_counts = {}

for char in string:
    if char.isalpha():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

for char, count in char_counts.items():
    print(f"{char}: {count}")
    
print("Non-repeating characters:", [char for char, count in char_counts.items() if count == 1])