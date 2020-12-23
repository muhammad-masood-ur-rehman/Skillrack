Top Ranking Student - Maths Physics Chemistry
The program must accept the marks scored by N students in Maths, Physics and Chemistry and print the name of the single top ranking student. 
- In case two students have scored same total marks, consider Maths marks. The student who has scored higher in Maths is the top ranking student. 
- In case two students have scored same total marks and have Maths marks equal, consider Physics marks. 
- In case two students have scored same total marks and have Maths and Physics marks equal, consider Chemistry marks. 
Input Format: The first line contains N. N lines follow with each line containing Name and marks in Maths, Physics, Chemistry of a specific student (the values are separated by a space).
Output Format: The first line contains the name of the top ranking student.
Boundary Conditions: 1 <= N <= 20 
Example Input/Output 1: 
Input: 
3 
Arundathi 100 90 85 
Bhuvana 100 95 80 
Chandan 100 95 78 
Output: 
Bhuvana
num=int(input())
li=[]
for ele in range(num):
    name,maths,physics,chemistry=map(str,input().split())
    total=int(maths)+int(physics)+int(chemistry)
    li.append([total,int(maths),int(physics),int(chemistry),name])
li.sort(reverse=True)
print(li[0][-1])
