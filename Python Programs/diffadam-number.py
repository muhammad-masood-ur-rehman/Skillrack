Diffadam number
A number ‘n’ is said to be a Diffadam number if the absolute value of the difference between the number ‘n’ and the reverse of ‘n’ is zero. For example, 121 is Diffadam number. The reverse of a number is the number got by writing the digits of the number in the reverse order (from right to left). Reverse of 132 is 231. 
Write an Algorithm and the subsequent Python code to check whether the given number is a Diffadam number or not. Write a function to reverse a number
Input Format: The first line will contain the number. 
Output Format: Print Diffadam number or Not a Diffadam number.
def rev(n):
 return(int(str(n)[::-1]))
 
def diffadam(num):
 if(num==rev(num)):
  print('Diffadam number')
 else:
  print('Not a Diffadam number')
  
n=int(input())
diffadam(n)
