my_age = 29

def func():
    my_age +=3
    return my_age

print(func())
#This will yield an error b/c python runs heavily on code scope
#b/c my_age = 29 is outside the function
#my_age within the function treats it as a new variable that has the same name as the first
#error is due to the my_age in the function was not declared. 
