list_of_numbers = [2, 10, 8, 3]
largest = 0


for number in list_of_numbers:
   
    if number > largest:
        largest = number
print("The current number is:" + str(number))
print("The current largest number is:" +  str(largest))