Array - Next Greater Element [Zoho]
Given an array of positive integers, print the next greater element for every element in the Array.
The next greater element for a given element X is the first greater element on the right side of X in the Array. If the element X does not have a greater element, print -1 for X.
Input Format:
The first line contains N, which denotes the number of elements in the Array.
The second line contains N positive integers, each separated by a space.
Output Format:
The first line contains the N integers which represent the next greater elements, each separated by a space.
Boundary Conditions:
1 <= N <= 10000
Example Input/Output 1:
Input:
4
4 5 2 25
Output:
5 25 25 -1
Example Input/Output 2:
Input:
5
10 9 8 7 6
Output:
-1 -1 -1 -1 -1
def printNGE(arr, n): 
    s = list() 
    arr1 = [0 for i in range(n)] 
    for i in range(n - 1, -1, -1):  
        while (len(s) > 0 and s[-1] <= arr[i]): 
            s.pop() 
        if (len(s) == 0): 
            arr1[i] = -1        
        else: 
            arr1[i] = s[-1]      
  
        s.append(arr[i]) 
    for i in range(n): 
        print(arr1[i],end=" ") 
m=int(input())
arr = list(map(int,input().split())) 
n = len(arr) 
printNGE(arr, n) 
