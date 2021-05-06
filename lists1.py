favorite_characters = []
favorite_characters.append('Batman')
favorite_characters.append('Wonderwoman')
favorite_characters.append('Thor')
favorite_characters.append('Aquaman')
favorite_characters.append('Blackpanther')

#print(favorite_characters[2])

index = 0

#print(len(favorite_characters))

#here is my WHILE loop
# it has a start at index,
# and finishes at the end of the list
print('-------WHILE LOOP------')
while index < len(favorite_characters):
    print(favorite_characters[index])
    index = index + 1

#here is a FOR loop
print ('-----FOR LOOP----')
for characters in favorite_characters:
    print(characters)


# FOR every single item, which i am calling "characters"
# that exits in my collection of items, called "favorite_characters"
# print that single item's value

