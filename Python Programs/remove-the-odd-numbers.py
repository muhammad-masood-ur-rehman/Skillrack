Remove the odd numbers
A number N is passed as  input. The program must remove all the odd digits in the passed number and display the number. If there are no odd digits in N, it must print "-1".
Input Format:
A number is passed as input.
Output Format:
Input number without any odd digits is printed.
Example Input/Output 1:
Input:
1234
Output:
24
Explanation:
Number N without odd numbers = 24
Example Input/Output 2:
Input:
22468
Output:
-1
Explanation:
Since there are no odd numbers in N, -1 is printed.
l=list(input().strip());s=''
c=0
for i in l:
  if int(i)%2==1:
    c+=1
  else:s+=i
if c>0 and len(s)>0:
  print(s)
else:
  print(-1)
