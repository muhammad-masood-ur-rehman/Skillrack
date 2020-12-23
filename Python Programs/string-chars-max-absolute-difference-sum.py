String Chars - Max Absolute Difference Sum
Max Absolute Difference Sum: Given N strings containing lower case alphabets as input, the program must print the string with the maximum sum of the absolute value of differences between every two consecutive characters in the string. If more than one string has the same sum, then print the last occurring string.
Boundary Condition(s):
1 <= N <= 50
1 <= Length of each string <= 100
Input Format:
The first line contains the value of N.
The next N lines contain a string each.
Output Format:
The first line contains a string.
Example Input/Output 1:
Input:
5
sun
noon
back
light
front
Output:
front
Explanation:
For the string sun, s-u + u-n = 19-21 + 21-14 = 9.
For the string noon, n-o + o-o + o-n = 14-15 + 15-15 + 15-14 =2.
For the string back, b-a + a-c + c-k = 2-1 + 1-3 + 3-11 = 11.
For the string light, l-i + i-g + g-h + h-t = 12-9 + 9-7 + 7-8 + 8-20 = 18.
For the string front, f-r + r-o + o-n + n-t = 6-18 + 18-15 + 15-14 + 14-20 = 22.
The string with maximum sum is front.
Example Input/Output 2:
Input:
4
vsn
ghijko
hp
cab
Output:
hp
Explanation:
For the string vsn, v-s + s-n = 22-19 + 19-14 = 8.
For the string ghijko, g-h + h-i + i-j + j-k + k-o = 7-8 + 8-9 + 9-10 + 10-11 + 11-15 = 8.
For the string hp, h-p = 8-16 = 8.
For the string cab, c-a + a-b = 3-1 + 1-2 = 3.
The last string with maximum sum is hp.
a=int(input())
b=[]
for i in range(a):
    b.append(*input().split())
maxi=0
c=""
for i in b:
    s=0
    j=0 
    while(j<len(i)):
        if(j+1<len(i)):
            s+=abs(ord(i[j])-ord(i[j+1]))
        j+=1
    if s>=maxi:
        maxi=s 
        c=i
print(c)
