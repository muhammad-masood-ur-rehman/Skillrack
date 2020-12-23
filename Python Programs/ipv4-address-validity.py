IPv4 Address Validity
Given an IPv4 address as a string, check if the address is valid. Print Valid if the address is valid else print Invalid. IPv4 address has 4 blocks of 8 bit (unsigned) numbers ranging from 0 to 255 separated by a . (dot).
Boundary Condition(s):
1 <= Length of address <= 50
Input Format:
The first line contains the IP address.
Output Format:
The first line contains Valid or Invalid.
Example Input/Output 1:
Input:
127.0.0.1
Output:
Valid
Example Input/Output 2:
Input:
266.2.9.34.12
Output:
Invalid
Explanation:
As 266 is present in the IP address
a=input().split(".")
if(len(a)==1):
    print("Invalid")
else:
    c=0
    for i in a:
        if i=="":
            print("Invalid")
            exit()
        if int(i)>= 0 and int(i)<= 255:
            c+=1
        else:
            print("Invalid")
            exit()
    print ("Valid")
