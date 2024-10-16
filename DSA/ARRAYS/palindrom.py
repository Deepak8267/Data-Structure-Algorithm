# Python3 program to check if a number is Palindrome
import array
# Function to check Palindrome
'''def check_palindrome(n):
   """ reverse = 0
    # Copy of the original number so that the original
    # number remains unchanged while finding the reverse
    temp = n
    while temp != 0:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
    # If reverse is equal to the original number, the
    # number is palindrome
    return reverse == n""""""
   
  
   reversed_value = n[::-1]
   return reversed_value
   

# Sample Input
n = 12321
n =str(n)
if check_palindrome(n) == n:
      print("Yes")
else:
      print("No")'''

'''v =int(input("Give me no value"))
t=0
for i in range(len(v)):
    t =+ v[i
n = str(v)
t = 0
for i in n:
    t  += int(i)
print(t)    
'''
# Rotate the array
'''arr = [1,2,3,4,5]
d = 2
for i in range(0,d):
    temp = arr[0]
    for j in range(0, len(arr)-1):
        arr[j] = arr[j+1]
    arr[len(arr)-1] = temp
print(arr)'''
A =[1,2,3,4,5]
D = 2
N = len(A)
temp = A[0:D]
for i in range(0, N-D):
    A[i] = A[i+D]
for j in range(N-D, N-1)

print(A)

    
print(temp)    
