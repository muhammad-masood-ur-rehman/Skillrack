Check First & Last Two Digits
Check First & Last Two Digits: Accept a number N and print "yes" if the first two digits and the last two digits are same, otherwise print "no".
Input Format:
The first line contains a number N.
Output Format:
The first line contains the "yes" or "no" based on the above mentioned condition.
Boundary Conditions:
9 <= N <= 9999999
Example Input/Output 1:
Input:
155215
Output:
yes
Example Input/Output 2:
Input:
9217623
Output:
no
n=input()
a=n[:2]
b=n[-2:]
print ("yes" if a==b else "no")
