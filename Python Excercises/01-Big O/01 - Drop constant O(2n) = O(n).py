#Consider the O(n) example

def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

    for k in range(n):
        print(k)

print_items(10)

# So the above code print 0-9 three times
# this denoted as O(3n)
# Here we need to drop the constant
# and it is considered as O(n)
# which is the exactly same  