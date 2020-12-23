Morse Code - Words
Morse Code - Words: A spaceship has exploded in the space and two survivors need to communicate with the station in the earth. Due to voice communication failure, they can hear only beep sound. Each consecutive beep sound denotes an alphabet. For example, two consecutive beep sound means the alphabet b. The beep sounds are represented as 1's. Group of consecutive 1's are given as input in each line. Help the crew to decode the message.
Note: Read the input carefully to avoid errors.
Boundary Condition(s):
1 <= Number of lines <= 100
1 <= Number of 1's in a line <= 1000
Input Format:
The list of lines contain group of consecutive 1's separated by space(s).
Output Format:
The first line contains the corresponding alphabet of each consecutive 1's separated by a space.
Example Input/Output 1:
Input:
111 1 11111111111111
1111111111111111111111111 111111111111111 111111111111111111111
11111111 11111 1 111111111111111111
1111111111111 11111
Output:
can you hear me
Explanation:
The word "can" is formed from the morse code 111 1 11111111111111
111 represents c
1 represents a
11111111111111 represents n
The word "you" is formed from the morse code 1111111111111111111111111 111111111111111 111111111111111111111
1111111111111111111111111 represents y
111111111111111 represents o
111111111111111111111 represents u
The word "hear" is formed from the morse code 11111111 11111 1 111111111111111111
11111111 represents h
11111 represents e
1 represents a
111111111111111111 represents r
The word "me" is formed from the morse code 1111111111111 11111
1111111111111 represents m
11111 represents e
Example Input/Output 2:
Input:
11 1111111 1111
1111111 111111111111 1
11111 11111111 11 1111111 11111111 111
11 11111111 1111 11111111
1 11 11 1
Output:
bgd gla ehbghc bhdh abba
while True:
    try:
        l=input().split()
        for i in l:
            print(chr(len(i)+96),end="")
        print(end=" ")
    except EOFError:
        break
