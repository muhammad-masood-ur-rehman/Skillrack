Eve number
A number ‘n’ is said to be an Eve number if the reverse of the square of the number ‘n’ is   not the square of the reverse of  ‘n’. For example, 15 is an Eve number.Square of 15 = 225Reverse of 15 = 51Square of 51= 2601 which is not the reverse of square of 15Write an Algorithm and the subsequent Python code to check whether the given number  is an Eve number or not.Write a function to reverse a number
Input Format:
The first line will contain the number.
Output Format:
Print Eve number or Not an Eve number
#Function to find the reverse of a number
def rev(n):
 return(int(str(n)[::-1]))

n=int(input())
if(n<0):
 print('Not an Eve number')
 exit()
if(rev((n)**2)==(rev(n))**2):
 print('Not an Eve number')
else:
 print('Eve number')
