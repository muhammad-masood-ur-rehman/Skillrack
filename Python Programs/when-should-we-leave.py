When should we leave
Your mother will take you to the doctor’s clinic for a check-up. She asks the time by which you have to book a taxi. Your mother has some works :  going to the dry-cleaners in the mall, have lunch in the restaurant, buy some dog food at the pet-shop, take money in the bank,  to be done on the way,
It takes 'x' minutes to drive to the mall and park the vehicle, and 'y' minutes to get the clothes dry cleaned, ‘z' minutes for lunch, 'a' minutes to get dog food, 'b' minutes to get money at the bank and 'c' minutes to drive to the doctor’s office from the mall.  Given the values for ‘x’, ‘y’, ‘z’, ‘a’ and ‘b’ and the time of appointment as 'h' hour 'm' minutes, write an algorithm and the subsequent Python code to determine when you should leave home. For example if x is 20, y is 10, z is 45, a is 10, b is 10, c is 20 and h is 14 and m is 0,  then you have to start from home by 12 hour 05 minutes.
Write appropriate functions for accomplishing the task.
Input Format:
First line contains the value for ‘x’
Next line contains the value for ‘y’
Next line contains the value for ‘z’
Next line contains the value for ‘a’
Next line contains the value for ‘b’
Next line contains the value for ‘c’
Next line contains the value for ‘h’
Next line contains the value for ‘m’
Output Format:
Print the start time from home in ‘hours’ and ‘minutes’ in 24 hour format.  
Hours and minutes shall be separated by a space.
Program:
data = []
for i in range(8):
    data.append(int(input().rstrip()))
hrs = 0
mini = 0
total_min = 0
for i in range(6):
    total_min += data[i]
hrs = total_min//60
mini = total_min%60
hrs = data[-2] - hrs
mini = data[-1] - mini
if mini < 0:
    mini = mini + 60
    hrs -= 1

print(hrs,mini)
