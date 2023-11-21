# even the O(2n) = O(100n) = O(n) called as Drop constants
# whatever the code may be, 
# the operation executes 10 times in Drop constants
def print_items(n):
    for i in range(n):
        for j in range(n):  # O(n²) = Dominant term
            print(i,j)
    
    for k in range(n):      # O(n) = Non-Dominant term
        print(k)

print_items(10)
# In Drop Non-Dominants as above code 
# O(n²) + O(n) = O(n² + n)
# the (n) will not be considered compared to (n²)
# which gives O(n² + n) = O(n²)
# the (n) is not that much big compared to (n²).