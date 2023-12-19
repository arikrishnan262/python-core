# python program to demonstrate
# creation of array

# importing "array" for array creations
import array as arr

# creating an array with integer type
a = arr.array('i', [1,2,3])

# printing original array
print("The new created is:", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
    

# creating an array with double type
b = arr.array('d', [2.5,3.2,3.3])

# printing original array
print("\n The new created array is :",end=" ")
for i in range(0,3):
    print(b[i],end=" ")
