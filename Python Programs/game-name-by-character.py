Game Name by Character
Game Name by Character: The program must accept a character CH (Lowercase) as input and print as per the following conditions.
If CH is a, print Athletics,
If CH is b, print Basketball,
If CH is c, print Cricket,
If CH is d, print Discus throw,
If CH is g, print Golf,
If CH is h, print Hockey,
If CH is f, print Football,
If CH is t, print Tennis,
For any other value print Invalid.
Boundary Condition(s):
a <= CH <= z
Input Format:
The first line contains the value of CH.
Output Format:
The first line contains any of the following values Athletics, Basketball, Cricket, Discus throw, Golf, Hockey, Football, Tennis or Invalid.
Example Input/Output 1:
Input:
h
Output:
Hockey
Example Input/Output 2:
Input:
e
Output:
Invalid
ch=str(input())
ch=ch.lower()
if ch=='a':print("Athletics")
elif ch=='b':print("Basketball")
elif ch=='c':print("Cricket")
elif ch=='d':print("Discus throw")
elif ch=='g':print("Golf")
elif ch=='h':print("Hockey")
elif ch=='f':print("Football")
elif ch=='t':print("Tennis")
else:print("Invalid")
