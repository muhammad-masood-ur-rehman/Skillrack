Vowelgram
Vowelgrams are words or sentences that has every vowel (a,e,i,o,u)  of  the English alphabet occurring  at the most  once. Write an algorithm and  a subsequent Python code to check whether a string is a vowelgram or not. Write a function to check if a given string is a vowelgram. For example,”You black tiger" is a vowelgram.
Input format
First line contains the string to be checked
Output Format
Print Vowelgram or Not vowelgram
def is_vowelgram(p):
 temp=0
 if(p.count('a')<=1 and p.count('e')<=1 and p.count('i')<=1 and p.count('o')<=1 and p.count('u')<=1):
  temp=1
 return temp

s=input().lower()
if(is_vowelgram(s)==1):
 print('Vowelgram')
else:
 print('Not Vowelgram')
