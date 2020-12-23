Smarty Affix Zeroes
Smarty Affix Zeroes: The program must accept two integers M and N as the input. The program must print the integers from M to N with smarty affix zeroes as the output.
Boundary Condition(s):
1 <= M < N <= 10^8
Input Format:
The first line contains M and N separated by a space.
Output Format:
The first line contains the integers from M to N with smarty affix zeroes.
Example Input/Output 1:
Input:
8 103
Output:
008 009 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 027 028 029 030 031 032 033 034 035 036 037 038 039 040 041 042 043 044 045 046 047 048 049 050 051 052 053 054 055 056 057 058 059 060 061 062 063 064 065 066 067 068 069 070 071 072 073 074 075 076 077 078 079 080 081 082 083 084 085 086 087 088 089 090 091 092 093 094 095 096 097 098 099 100 101 102 103
Example Input/Output 2:
Input:
990 1020
Output:
0990 0991 0992 0993 0994 0995 0996 0997 0998 0999 1000 1001 1002 1003 1004 1005 1006 1007 1008 1009 1010 1011 1012 1013 1014 1015 1016 1017 1018 1019 1020
a,b=map(int,input().split())
c=len(str(b))
for i in range(a,b+1):
    print(str(i).zfill(c),end=" ")
