import array

# Creation  an  blank array with total size is 5

"""new_arr = array.array('I', [0]*(5)).tolist()   
print(len(new_arr))"""


# Implementation of Array

"""arr_int = array.array('I', [1,2,3,4,5])
print("Integer array " , arr_int.tolist())
# Traversal of Array
for x in arr_int:
    print(x)"""

# Insertion Of array with unsorted array no order maintain

"""arr = array.array('I',[1,5,4,2,8,6])
x = 10
pos = 2
n = len(arr)

def insertElment(arr,pos,x):
    if pos < 0 or pos > n:  # Validate the position
        raise IndexError("Index is out of range")

    new_arr = array.array(arr.typecode, [0]*(n+1))
    o = len(new_arr)
    # Copy elemtn to the new array
    for i in range(pos):  
        new_arr[i] = arr[i]
    new_arr[pos] = x 
    for i in range(pos, n):
        new_arr[i+1] = arr[i]
   
    

    return new_arr    

art=insertElment(arr,pos,x)
print(art.tolist()) """

# Insertion of array with unsorted array no order maintain

"""arr = array.array('I',[1,5,4,2,8,6])
x = 10

def insertElment(arr,x):
    arr.append(x)
    
insertElment(arr,x)
print(arr) """


# Deletion with oder maintain with unsorted array

""""arr = array.array('I',[1,5,4,2,8,6])
delv = 8  
n = len(arr)

def findElement(arr, delv):
    for i in range(len(arr)):
        if arr[i] == delv:
            return i



def deleteElment(arr):
    pos = findElement(arr, delv)
   

    new_arr = array.array(arr.typecode, [0]*(n-1))
    o = len(new_arr)
    # Copy elemtn to the new array
    for i in range(pos):  
        new_arr[i] = arr[i] 
    for i in range(pos + 1, n):
        new_arr[i-1] = arr[i]
   
    

    return new_arr  
art=deleteElment(arr)
print(art.tolist()) 
"""

# Reversed array
arr = array.array('I', [1,2,3,4,5])
rev_arr = arr[::-1]
print(rev_arr)