Polynomial Addition
Write an algorithm and the subsequent Python program to add the two given polynomials. Assume that the coefficients of each polynomial are stored in a separate list.
d=int(input())
p1=[]
p2=[]
for i in range(d+1):
 c=int(input())
 p1=[c]+p1    #first element is the coefficient of x^0
d=int(input())
for i in range(d+1):
 c=int(input())
 p2=[c]+p2    #first element is the coefficient of x^0
l1=len(p1)
l2=len(p2)
greater_degree=l2;  #let
pf=[]  #final list with the sum of coefficients


#Reversing the list
p1.reverse()   #first element is the coefficient of x^n
p2.reverse()   #first element is the coefficient of x^n


if(l1>l2):
 greater_degree=l1;
 for i in range(l1-l2):
  p2=[0]+p2
else:
 for i in range(l2-l1):
  p1=[0]+p1
for i in range(greater_degree):
 pf.append(p1[i]+p2[i])
print(pf)
