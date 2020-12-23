Automorphic Numbers
Automorphic numbers are numbers having "n" digits such that the last n digits of the square of the number will be the number itself. Write an algorithm and the subsequent Python code to check if the given number is automorphic. Write a function to find the square of a given number. For example, 25 is a 2 digit automorphic number with a square of 625 and 376  with its square 141376, which is a 3 digit automorphic number.
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
 print('Automorphic')
else:
 print('Not automorphic')
