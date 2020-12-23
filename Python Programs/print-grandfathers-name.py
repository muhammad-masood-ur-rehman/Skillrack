Print Grandfather's Name
The program must accept first and last names of three persons who are in a family tree and print the grandfather's name. 
Input Format: 
The first line contains the first and last name of person 1 separated by a space. 
The second line contains the first and last name of person 2 separated by a space. 
The third line contains the first and last name of person 3 separated by a space. 
Output Format: The first line contains the first and last name of the grandfather separated by a space. 
Boundary Conditions: Length of first and last names are from 3 to 100 
Note: The last name of a person is nothing but the father's first name. 
Example Input/Output 1: 
Input: 
Arun Kumar 
Swamy Nathan 
Kumar Swamy 
Output: Swamy Nathan
a=input().strip()
b=input().strip()
c=input().strip()
if a.spilt()[-1] != b.split()[0] and a.split()[-1] != c.spilt()[0]:
    print(a)
if b.spilt()[-1] != a.split()[0] and b.split()[-1] != c.spilt()[0]:
    print(b) 
else:
    print(c)  
