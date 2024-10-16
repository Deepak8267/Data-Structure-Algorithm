# Binary search algorithm

"""arr = [2,4,8,12,14,16,18,20]
key = 16
low=0
high=len(arr)-1
while low <= high:
    mid = low+(high-low)//2
    if arr[mid] == key:
       print("key is presented with index ", {mid})
       break 
    elif arr[mid] < key:
        low = mid
    else:
           high = mid"""
class Person:
  def __init__(self, name, age):
    self.n = name
    self.a = age


n1 = input("Please enter the name:" )
a1 = input("Plase input the age:" )
p1 = Person(n1,a1)

print(p1.n)
print(p1.a)    