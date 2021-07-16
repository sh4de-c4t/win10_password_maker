# password_maker - klondak
import string
import random
import os

print('This Script Will Generate Secure Passwords for You!')
print('Coded by klondak')
print('#'*51)

def windows_copy_to_clipboard(text):
    command = f'echo | set /p="{text.strip()}"|clip'
    return os.system(command)


letters = string.ascii_letters
digits = string.digits
specials = string.punctuation
chars = letters + digits + specials

while True:
    length = int(input('Enter password length: '))

    password_chars = []
    for i in range(length):
        password_chars.append(random.choice(chars))

    password = ''.join(password_chars)
    if '"' not in password:
    	windows_copy_to_clipboard(password)
    else:
    	print('Your pass can not be copied to clipboard :(')

    print(f'Your password is\n{password}')
    print('#'*40)
