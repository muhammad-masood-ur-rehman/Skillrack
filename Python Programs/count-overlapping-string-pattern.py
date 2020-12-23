Count Overlapping String Pattern
Two string values S and P representing a string and pattern are passed as the input to the program. The program must print the number of overlapping occurrences of pattern P in the string S as the output.
Note: The string S and pattern P contains only lowercase alphabets.
Boundary Condition(s):
1 <= Length of S <= 2000000
1 <= Length of P <= 10
Input Format:
The first line contains S.
The second line contains P.
Output Format:
The first line contains the number of overlapping occurrences of P in S.
Example Input/Output 1:
Input:
precondition
on
Output:
2
Explanation:
The pattern on occurs two times in precondition so 2 is printed.
Example Input/Output 2:
Input:
tetetetmtey
tet
Output:
3
def overlap(string,substring):
    c=0;s=0
    while s<len(string):
        pos=string.find(substring,s)
        
        if pos!=-1:
            s=pos+1 
            c+=1 
        else:
            break
    return c
    
string=input().strip()
substring=input().strip()

print(overlap(string,substring))
