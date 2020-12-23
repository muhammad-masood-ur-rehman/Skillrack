Vowgram
Vowgrams are words or sentences that has every vowel of  the English alphabet occurring  at least  once. Write an algorithm and  a subsequent Python code to check whether a string is a vowgram or not. Write a function to check if a given string is a vowgram. For example, "The quick brown fox jumps over the lazy dog" is a vowgram.
def is_vogram(p):
 temp=0
 if(p.count('a')>=1 and p.count('e')>=1 and p.count('i')>=1 and p.count('o')>=1 and p.count('u')>=1):
  temp=1
 return temp

s=input().lower()
if(is_vogram(s)==1):
 print('Vowgram')
else:
 print('Not vowgram')
