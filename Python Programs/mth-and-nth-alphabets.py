Mth and Nth Alphabets
Mth and Nth Alphabets: The program must accept three integers M, N and K as the input. The program must form a string S of length K using the 26 lower case alphabets (a to z) based on the following conditions.
- The 1st alphabet of S must be the Mth alphabet in the lower case alphabets. Then the program must remove the Mth alphabet from the lower case alphabets.
- The 2nd alphabet of S must be the Nth alphabet in the remaining lower case alphabets. Then the program must remove the Nth alphabet from the lower case alphabets.
- The 3rd alphabet of S must be the Mth alphabet in the remaining lower case alphabets. Then the program must remove the Mth alphabet from the lower case alphabets.
- The 4th alphabet of S must be the Nth alphabet in the remaining lower case alphabets. Then the program must remove the Nth alphabet from the lower case alphabets.
- Similarly, the remaining alphabets of S must be formed using the remaining lower case alphabets.
Finally, the program must print the string S as the output.
Note: The English alphabet set must be considered in a cyclic fashion for the Mth and Nth alphabet.
Boundary Condition(s):
1 <= M, N <= 1000
1 <= K <= 26
Input Format:
The first line contains M, N and K separated by a space.
Output Format:
The first line contains the string S.
Example Input/Output 1:
Input:
5 8 10
Output:
eifkgmhojq
Explanation:
The 26 lower case alphabets are abcdefghijklmnopqrstuvwxyz.
M = 5, N = 8 and K = 10.
Here we need to form a string of length 10.
1st alphabet of S = 5th lower case alphabet e.
Now the remaining lower case alphabets are abcdfghijklmnopqrstuvwxyz.
2nd alphabet of S = 8th lower case alphabet i.
Now the remaining lower case alphabets are abcdfghjklmnopqrstuvwxyz.
3rd alphabet of S = 5th lower case alphabet f.
Now the remaining lower case alphabets are abcdghjklmnopqrstuvwxyz.
4th alphabet of S = 8th lower case alphabet k.
Now the remaining lower case alphabets are abcdghjlmnopqrstuvwxyz.
Similarly, the remaining 6 alphabets of S are formed using the remaining lower case alphabets.
The string S is eifkgmhojq, which is printed as the output.
Example Input/Output 2:
Input:
30 27 5
Output:
dbhfl
a='abcdefghijklmnopqrstuvwxyz'
m,n,k=map(int,input().split())
s='';i=1
for i in range(1,k+1):
    if i%2==1:l=(m-1)%len(a);s+=a[l];a=a.replace(a[l],'')
    else:l=(n-1)%len(a);s+=a[l];a=a.replace(a[l],'')
print(s)
