def first_fun(name):
    print("This is my first python function")
    print("Hello " + str(name))


first_fun("Prabhdeep")
first_fun(55)


def cube(num):
    return num * num * num


print("After return but before call")

print("Cub of 3 is: " + str(cube(3)))
