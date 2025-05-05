

# Example 1
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        # print(count)
        return count

    return increment


# # Create two separate counter instances
# print(id(counter)) 
counter1 = counter()
# print(id(counter1))
counter2 = counter()
# print(id(counter2))
#
a = counter1()
# print(id(a))
counter1()
# print(id(a))
b = counter1()
print(a)
print(b)


# counter2()

# Example 2
def new_append():
    new_list = []

    def appending(x):
        nonlocal new_list
        new_list.append(x)
        return new_list

    return appending


append1 = new_append()
append2 = new_append()
x1 = append1(4)
append1(5)
append1(7)
append1(8)
print(x1)

x2 = append2(6)
append2(3)
append2(1)
print(x2)
