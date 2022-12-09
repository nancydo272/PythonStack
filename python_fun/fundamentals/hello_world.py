# Write the code to print a literal string saying "Hello World" (#1)
print('Hello World')

#Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a comma in the print function
name = 'Nancy Do'
print('Hello', name, "!")

#Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a + in the print function (#2b)
print('Hello ' + name)

#Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a comma in the print function (#3a)

favNum = 12
print('Hello', favNum, '!')

#Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a + in the print function (#3b)
#Need to convert favNum into a string cause cannot add interger to a string
print('Hello '+ str(favNum) + '!')

#Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with the format method (#4a)

food1 = 'pho'
food2 = 'hotpot'
print('I love to eat {} and {}!'.format(food1,food2))

#Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with f-strings (#4b)

print(f'I love to eat {food1} and {food2}!')