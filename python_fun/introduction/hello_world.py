print("Hello World")

x = "Hello Python"
print(x)

int_to_float = float(35)
print(int_to_float)

#Concatening Strings
name = "Zen"
print("My name is", name)
print("My name is " + name)
#both will print My name is Zen. 
#if we change name = 1 -->will get type error

#f-string interpolation
first_name = "Zen"
last_name = "Coder"
print(f"My name is {first_name} {last_name}.")

#string.format()
print("My name is {} {}.".format(first_name, last_name))

#% Format
age = 27
print("My name is %s and I'm %d" % (first_name, age))	