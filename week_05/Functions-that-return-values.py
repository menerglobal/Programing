'''
def silly_square(x):
    k = - x * x
    return k

a = 5
b = silly_square(a)
print(b)
print(type(b))
print(type(silly_square))
'''
'''
def my_function(x, y):
    k = x + y
    if k > 10:
        return k
    return 0

print(my_function(3, 4))
print(my_function(30, 40))
'''
'''
def another_function(hours):
    if hours < 12:
        return "Good morning!"
    elif hours < 18:
        return "Good afternoon!"
    else:
        return "Goodbye!"

print(another_function(15))
'''
'''
def returning_expression(x):
    return x * 2 + 20

a = 10
b = returning_expression(a)
print(b)
'''
'''
def is_even(x):
    return x % 2 == 0
    
print("Is 5 even?", is_even(5))
print("Is 6 even?", is_even(6))
'''
'''
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
print(is_even(5))
'''
'''
def doing_two_things(name):
    print("Hello, " + name + "!")
    return "Your name is " + str(len(name)) + " characters long."
    
comment = doing_two_things("Michael")
print(comment)
'''

'''
def say_hello():
    print("Hello!")

a = say_hello()
print(a)
'''
#If the function doesn’t have a return statement, it will return None. This is why the second line of the printed output is None.










