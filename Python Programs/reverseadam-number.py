Reverseadam number
A number 'n' is said to be a Reversedam number if the number is divisible by its reverse.
#Function to find the reverse of a number
def rev(num):
 new=0
 while(num):
  f=len(str(num))
  new=new+(num%10)*10**(f-1)
  f-=1
  num=num//10
 return new

n=int(input())
r=rev(n)
if(n%r==0):
 print('Reverseadam number')
else:
 print('Not a reverseadam number')
