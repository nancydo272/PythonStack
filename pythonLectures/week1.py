# my_age = 29

# def func():
#     my_age +=3
#     return my_age

# print(func())
#This will yield an error b/c python runs heavily on code scope
#b/c my_age = 29 is outside the function
#my_age within the function treats it as a new variable that has the same name as the first
#error is due to the my_age in the function was not declared. 

#Slicing for srings, lists, tuples, dictionaries -> it includes the 0 but slice out at 5
f_name = 'Jonathon'
#         012345
print(f_name[0:5])
# --> Jonat
print(f_name[-1])
# --> n b/c it will loop backwards!!!!
print(f_name[-4]) # ---> t

my_hobbies = ['drumming', 'walking my dog', 'dancing', 'running']
print(my_hobbies[0:2])      # --> 'drumming', 'walking my dog'
print(my_hobbies[:])       # -->will print all the way to the end 

#Dictionaries 
student = {
    'f_name': 'Nancy',
    'l_name': 'Do',
}

for key in student:
    print(key)

#for dictionaris in for-loop, key is just a variable name it can be anything
#but b/c there is only 1 variable, it defaults to the key in the dictionary student -->f_name
#Need to call items and 2 variables to print out both or either one 
for key, values in student.items():
    print(values)
    print(key)
    print(f'Key {key} with value of {values}')

weekend = {'Sun': 'Sunday', 'Fri':'Friday','Sat': 'Saturday'} 

print(weekend) 



#delete values 2 Ways 

removed_value = weekend.pop('Sat') 

print(removed_value)    #Saturday 

print(weekend)                                 #{'Sun': 'Sunday', 'Fri': 'Friday'} 

 

del weekend['Fri']  

print(weekend)                                 #{'Sun': 'Sunday'} 

 

weekday = {'Mon':'Monday', 'Tue':'Tuesday', 'Wed':'Wednesday', 'Thur':'Thursday'} 

 

print(len(weekday))                        #4 

print(str(weekday)) 

print(type(weekday))      #<class 'dict'> 

 

#dictionary.items() -- returns a list of dictionary's (key, value) tuple pairs. 

print(weekday.items())   

                #dict_items([('Mon', 'Monday'), ('Tue', 'Tuesday'),                              ('Wed', 'Wednesday'), ('Thur', 'Thursday')]) 

     

print(weekday.keys()) 

                #dict_keys(['Mon', 'Tue', 'Wed', 'Thur']) 

     

print(weekday.values()) 

                #dict_values(['Monday', 'Tuesday', 'Wednesday', 'Thursday']) 

     

print(weekend.clear())  

                #none since it removes all elements from the dictionary 