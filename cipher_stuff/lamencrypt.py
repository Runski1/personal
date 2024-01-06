import os
from itertools import cycle


def txtfile_to_list(file_path):
    with open(file_path, "r") as file:
        string = file.read()
    string_as_list = []
    for char in string:
        num = next((key for key, value in character_dict.items() if value == char), None)
        if num is not None:
            string_as_list.append(str(num))
    return string_as_list


characters = (
    "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "
    "a b c d e f g h i j k l m n o p q r s t u v w x y z "
    "0 1 2 3 4 5 6 7 8 9 "
    ". , ; : ! ? ' \" ( ) [ ] { } - _ / \\ | @ # $ % ^ & * + = ~ ` "
)

# Create a dictionary with characters as values and keys as range from 0 onward
character_dict = {index: char for index, char in enumerate(characters.split())}
character_dict[92] = ' '  # don't know how to add space in characters-string
cwd = os.getcwd()
print(cwd)
key_list = txtfile_to_list(cwd + "/key.txt")
encrypted_list = txtfile_to_list(cwd + "/plaintext.txt")
print("encrypted list: ", encrypted_list)
print("key list: ", key_list)

# now the encoding part
encrypted_message_list = []
cycle_key_list = cycle(map(int, key_list))
for num1 in encrypted_list:
    num2 = next(cycle_key_list)  # I should look into itertools
    total = int(num1) + num2
    if total > 92:
        total %= 93  # Reset to 0 when it exceeds 92
    encrypted_message_list.append(str(total))

# Now we transform the number list to string
encrypted_string = ""
for num in encrypted_message_list:
    encrypted_string += character_dict[int(num)]
print("encrypted string: ", encrypted_string)
# decrypt part:
new_cycle_key_list = cycle(map(int, key_list))
ciphered_list = txtfile_to_list(cwd + "/encrypted_message.txt")
print("ciphered list: ", ciphered_list)
decrypted_list = []
for number1 in ciphered_list:
    number2 = next(new_cycle_key_list)
    total = int(number1) - number2
    if total < 0:
        total = 93 - abs(total)
    decrypted_list.append(str(total))
print(decrypted_list)
decrypted_string = ""
for number in decrypted_list:
    decrypted_string += character_dict[int(number)]
print(decrypted_string)
