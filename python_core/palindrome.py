num = int(input("Enter a number: "))
num_str = str(num)
if num_str == num_str[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


