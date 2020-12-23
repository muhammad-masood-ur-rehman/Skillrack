Square Even and Cube Odd
Square Even and Cube Odd: Given an array of integers of size N as input, the program must print the square of even elements and the cube of odd elements
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).
Output Format:
The first line contains N integers separated by a space.
Example Input/Output 1:
Input:
5
2 3 7 4 1
Output:
4 27 343 16 1
Explanation:
For 1st element 2 is an even number->2*2 so print 4
For 2nd element 3 is an odd number->3*3*3 so print 27
For 3rd element 7 is an odd number->7*7*7 so print 343
For 4th element 4 is an even number->4*4 so print 16
For 5th element 1 is an odd number->1*1*1 so print 1
Example Input/Output 2:
Input:
4
10 9 6 3
Output:
100 729 36 27
Explanation:
For 1st element 100 is an even number->10*10 so print 100
For 2nd element 9 is an odd number->9*9*9 so print 729
For 3rd element 6 is an even number->6*6 so print 36
For 4th element 3 is an odd number->3*3*3 so print 27
n=int(input())
l=list(map(int,input().split()))
for i in l:
        if i%2==0:
            print(i**2,end=" ")
        else:
            print(i**3,end=" ")
