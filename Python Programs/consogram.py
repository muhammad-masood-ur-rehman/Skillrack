Consogram
Consograms are words or sentences that has every consonant( letters other than a,e,i,o,u) of the English alphabet occurring at least once. Write an algorithm and a subsequent Python code to check whether a string is a consogram or not. Write a function to check if a given string is a consogram. For example,”"The quick brown fox jumps over the lazy dog"" is a consogram.
def cons(sen):
 sen=list(filter(lambda a: a != ' ', sen))
 q=['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
 flag=1
 for i in q:
  if(sen.count(i)<1):
   flag=0
 if(flag==1):
  print('Consogram')
 else:
  print('Not consogram')

sen=input().lower()
cons(sen)
