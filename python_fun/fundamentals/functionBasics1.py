#For each of the following code snippets, predict the output 

#1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())

#prediction: 5 
#output: 5

#2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#prediction: Error b/c of undefined variable 
#outcome: Error 

#3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())

#prediction: 5, only returns the first one. 

#4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())
#prediction:5 in the rerturn statement b/c its before the print statement  

#5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)            #this print statement is outside the function when no aurgment was given
#prediction: 5 and none

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

#prediction: 3 and 5 --> error b/c cannot add nonetypes
#NoneType = function that does not return anything 