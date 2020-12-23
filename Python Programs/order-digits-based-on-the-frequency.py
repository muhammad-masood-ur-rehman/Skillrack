Order digits based on the frequency
A string consists of digits from 1-9 will be passed as input. The program must print the digits sorted based on the number of occurrence. If one or more digits occur the same number of times, the smallest digit must be printed first.
Input Format: The first line will contain the N digits from 1-9
Boundary Conditions: 3 <= N <= 30
Output Format: The digits sorted based on the number of occurrence.
Example Input/Output 1:
Input:
4443338993
Output:
3333444998
Explanation: 3 occurs the most number of times (four times). Hence it is printed first. 4 occurs thrice and hence printed after the 3s. 9 occurs twice and hence printed after the 4s. 8 occurs only once and hence printed after 9.
Example Input/Output 2:
Input:
95559998228
Output:
99995552288
Explanation: Here 2 and 8 occurs twice. Hence 2 being the smaller digit is printed before 8.
n,l=int(input()),[]
while(n!=0):
    r=n%10
    l.append(r)
    n//=10
l1=sorted(sorted(l),key=l.count,reverse=True)

print("".join(str(i) for i in l1))
