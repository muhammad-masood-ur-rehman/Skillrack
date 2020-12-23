Adam number
A number is said to be an Adam number if the reverse of the square of the number is equal to the square of the reverse of the number.  For example, 12 is an Adam number because the reverse of the square of 12 is the reverse of 144, which is 441, and the square of the reverse of 12 is the square of 21, which is also 441.
Write an Algorithm and the subsequent Python code to check whether the given number  is an Adam number or not.
Write a function to reverse a number
def rev(n):
 return(int(str(n)[::-1]))
 
def adam(num):
 if(rev(num)**2==rev(num**2)):
  print('Adam number')
 else:
  print('Not an Adam number')
  
n=int(input())
adam(n)
