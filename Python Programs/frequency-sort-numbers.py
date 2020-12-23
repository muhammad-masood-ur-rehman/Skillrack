Frequency Sort - Numbers
Given N integers, sort them based on their frequency in descending order. If the frequency is same then sort based on their values in ascending order.
Boundary Condition(s):
1 <= N <= 10000
Input Format:
The first line contains N.
The second line contains N integers separated by space.
Output Format:
The first line contains N integers sorted by their frequency in descending order and their values in ascending order separated by space.
Example Input/Output 1:
Input:
8
2 1 2 8 7 3 7 2
Output:
2 2 2 7 7 1 3 8
Example Input/Output 2:
Input:
5
5 4 3 2 1
Output:
1 2 3 4 5
def sortByFreq(arr, n): 
	maxE = -1;
	for i in range(n): 
		maxE = max(maxE, arr[i])
	freq = [0]*(maxE + 1); 
	for i in range(n): 
		freq[arr[i]] += 1;
	cnt = 0;
	for i in range(maxE+1): 
		if (freq[i] > 0): 
			value = 100000 - i; 
			arr[cnt] = 100000 * freq[i] + value; 
			cnt += 1;
	return cnt;
def printSortedArray(arr, cnt): 
	for i in range(cnt): 
		frequency = arr[i] / 100000; 
		value = 100000 - (arr[i] % 100000); 
		for j in range(int(frequency)): 
			print(value, end=" ") 
			
num=int(input())
arr=list(map(int,input().split()))
n = len(arr)
cnt = sortByFreq(arr, n);
arr.sort(reverse = True) 
printSortedArray(arr, cnt);
