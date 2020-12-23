Heterosquare Numbers
Heterosquare numbers are the numbers having "n" digits such that the last n digits of the square of the number will not be the number itself. .Write an algorithm and the subsequent Python code to check if the given number is a Heterosquare number. Write a function to find the square of a given number. For example, 22 is a 2 digit heterosquare number with a square of 484 and 111 with its square  12321, is a 3 digit heterosquare number.
def sqr(n):
 return(n*n)

n=int(input())
c=sqr(n)
s=0
m=len(str(n))
L=len(str(n))
for i in range(L):
 s+=(c%10)*(10)**i
 m-=1
 c//=10
if(s==n):
 print('Not Heterosquare')
else:
 print('Heterosquare')
