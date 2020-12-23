Shift an array towards right
An array with N numbers is passed as input to the program. The program must shift the values in the array to the right by one place.
Then the program must print the modified value as output.
Input Format:
The first line will contain the value of N.
The next N lines will contain the value of the N elements in the array.
Example Input/Output 1:
Input:
5
100
200
300
400
500
Output:
500
100
200
300
400

Example Input/Output 2:
Input:
3
22
33
44
Output:
44
22
33
n=int(input())
lst=[]
for i in range(n):
    m=lst.append(int(input()))
e1 = lst[-1]
for i, e2 in enumerate(lst):
    lst[i], e1 = e1, e2
print(*lst,sep="\n")
