
# take user input to be encrypted
message = input("Please enter string to encrypt: ")

# take input for offset
offset = int(input("please enter an offset value (1 to 94): "))

# where the encrypted message will go
encrypted = ""

for letter in message:
    if ord(letter) + offset > 126:
        encrypted += chr(ord(letter) + offset - 95)
    else:
        encrypted += chr(ord(letter) + offset)
print(encrypted)