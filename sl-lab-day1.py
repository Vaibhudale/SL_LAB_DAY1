# Python program to  
# demonstrate numeric value 
  
a = 5
print("Type of a: ", type(a)) 
  
b = 5.0
print("\nType of b: ", type(b)) 
  
c = 2 + 4j
print("\nType of c: ", type(c))
##program to demonstrate strings
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
## program to demonstrate typecasting
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

