Smallest number by rearranging digits of a given number
Find the Smallest number (Not leading Zeros) which can be obtained by rearranging the digits of given number.
Input: 846903
Output: 304689

Input: 55010
Output:10055
from collections import Counter
s=''.join(sorted(input()))
x=s.rfind('0')         //find the last index
c=Counter(s)       //get the frequency 
y=list(c.values())[1]    //get the [1]particular index value
print(s[x+1:(y+x)+1],s[0:x+1],s[(x+y)+1:],sep="")
