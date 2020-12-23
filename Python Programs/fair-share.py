Fair Share
Fair Share - Problem Statement:
Raju and Kumar are friends and they order S items in a hotel but Kumar does not eat the Ith item ordered. Raju eats the Ith item alone. They decide to share the cost of all items they share and eat. The amount paid by Kumar is also passed as the input. If the bill amount is split equally after deducting the Ith item price the program must print "FAIR SHARE" otherwise the program must print the absolute difference between amount paid by Kumar and the half of the amount for the items shared by Raju and Kumar.
Input Format:
First line contains S & I [S - Number of Items & I - the item ate by Raju alone].
Second line contains items cost separated by space.
Third line contains the amount paid by Kumar
Output Format:
First Line contains "FAIR SHARE" or the absolute difference between the amount paid by Kumar and the half of the amount for the items shared by Raju and Kumar rounded up to 1 decimal place.
Example Input/Output 1:
Input:
7 4
12 3 7 34 12 4 8
30
Output:
7.0
Example Input/Output 2:
Input:
5 3
40 20 11 6 8
37
Output:
FAIR SHARE
Example Input/Output 3:
Input:
4 4
15 10 20 25
25
Output:
2.5
a,b=map(int,input().split())
l=list(map(int,input().split()))
d=int(input())
s=0
for i in range(0,a):
    if i!=b-1:s+=l[i]
if s//2==d:
    print('FAIR SHARE')
else:
    print(abs(d-s/2))
