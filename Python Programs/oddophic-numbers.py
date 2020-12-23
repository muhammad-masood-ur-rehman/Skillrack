Oddophic Numbers
Given ‘n’ integers, write an algorithm and the subsequent Python code to print all numbers that are oddophic to the first number. Two numbers with non-distinct (numbers in which digits get repeated) digits are said to be oddophic if they have the same number of digits in it and the sets of positions having the same digits contains only odd positions. Positions of digits are numbered from left to right starting from 1.
def same_pos(p):
 p=str(p)
 pos=[]
 for i in range(len(p)-1):
  for j in range(i+1,len(p)):
   if(p[i]==p[j]):
    pos.append(int(i)+1)
    pos.append(int(j)+1)
 return pos

def odd_list(p1):
 flag=1
 for i in p1:
  if(int(i)%2==0):
   flag=0
 return flag 

def oddo(num1,num2):
 f=0
 if(len(num1)==len(num2)):
  if(same_pos(num1)!=[] and same_pos(num2)!=[]):
   if(odd_list(same_pos(num1))==1 and odd_list(same_pos(num2))==1):
    f=1
 return(f)
 
n=int(input())
list_of_n=[]
print_list=[]
for i in range(n):
 list_of_n.append(int(input()))
flag=0 
for i in range(len(list_of_n)):
 if(oddo(str(list_of_n[0]),str(list_of_n[i]))==1):
  flag=1
  print_list.append(list_of_n[i])
if(flag==0):
 print('No oddophic')
else:
 for i in print_list:
  print(i)
