Autocube Numbers
Autocube numbers are numbers having "n" digits such that the  last n digits of the cube  of the number will be the number itself. Write an algorithm and the subsequent Python code to check if the given number is autocube. Write a function to find the cube of a given number.. For example, 25 is a 2 digit autocube number with a cube  of 15625 and 376  with its  cube  53157376, is a 3 digit autocube number.
Input Format: First line contains the number to be checked
Output Format: Print Autocube or Not autocube
def cube(n):
 return(n*n*n)

n=int(input())
c=cube(n)
s=0
m=len(str(n))
L=len(str(n))
for i in range(L):
 s+=(c%10)*(10)**i
 m-=1
 c//=10
if(s==n):
 print('Autocube')
else:
 print('Not autocube')
