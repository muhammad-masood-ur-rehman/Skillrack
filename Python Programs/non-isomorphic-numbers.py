Non-Isomorphic Numbers
Given ‘n’ integers, write an algorithm and the subsequent Python code to print all numbers that are Non-isomorphic to the first number. Two numbers with non-distinct digits ( numbers in which digits are repeated)  are said to be non-isomorphic if they have the same number of digits in it and the sets of positions  having the same  digits are different. 
def same_pos(p):
 pos=[]
 for i in range(len(p)-1):
  for j in range(i+1,len(p)):
   if(p[i]==p[j]):
    pos.append((i,j))
 return pos

def same_list(p1,p2):
 flag=0
 if(p1!=p2):
  flag=1
 return flag

def non_iso(num1,num2):
 f=0
 if(len(num1)==len(num2)):
  if(same_pos(num1)!=[] and same_pos(num2)!=[]):
   if(same_list(same_pos(str(num1)),same_pos(str(num2)))==1):
    f=1
 return(f)
 
n=int(input())
list_of_n=[]
print_list=[]
for i in range(n):
 list_of_n.append(int(input()))
flag=0 
for i in range(len(list_of_n)):
 if(non_iso(str(list_of_n[0]),str(list_of_n[i]))==1):
  flag=1
  print_list.append(list_of_n[i])
if(flag==0):
 print('No non-isomorphic')
else:
 print(list_of_n[0])
 for i in print_list:
  print(i)
