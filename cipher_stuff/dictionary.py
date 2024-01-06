characters = (
    "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "
    "a b c d e f g h i j k l m n o p q r s t u v w x y z "
    "0 1 2 3 4 5 6 7 8 9 "
    ". , ; : ! ? ' \" ( ) [ ] { } - _ / \\ | @ # $ % ^ & * + = ~ `"
)

# Create a dictionary with characters as values and keys as range from 0 onward
character_dict = {index: char for index, char in enumerate(characters.split())}

# Print the dictionary
print(character_dict)