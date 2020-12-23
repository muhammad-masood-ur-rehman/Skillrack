Finding a Friend with Longest Name
Write an algorithm and the subsequent Python program to store the names of your friends, count the number of friends, identify the longest name and the number of letters in the longest name. Get the names of friends till 'stop' is entered. For example, if the input sequence is Ravi, Raj, Puela, stop, then the output is 3, Puela and 5.

When you are coding in the online judge (SkillRack), use rstrip() function to remove carriage return from the input string.

Input Format:
First line is the name of the first friend
Second line is the name of the second friend
Third line is the name of the third friend
….
stop

Output Format:
Number of friends
Friend’s name with longest length
Number of characters in that longest name
list_of_names=[]
name=input().rstrip()
while(name!="Stop"):
 list_of_names.append(name)
 name=input().rstrip()
print(len(list_of_names))
temp=""
m=0
for name in list_of_names:
 if(len(name)>m):
  m=(len(name))
  temp=name
print(temp)
print(m)
