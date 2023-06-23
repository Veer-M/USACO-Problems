'''
Description:

Several seasons of hot summers and cold winters have taken their toll on Farmer John's fence, and he decides it is time to repaint it, along with the help of his favorite cow, Bessie.
Unfortunately, while Bessie is actually remarkably proficient at painting, she is not as good at understanding Farmer John's instructions.
If we regard the fence as a one-dimensional number line, Farmer John paints the interval between x=a and x=b.
For example, if a=3 and b=5, then Farmer John paints an interval of length 2.
Bessie, misunderstanding Farmer John's instructions, paints the interval from x=c to x=d, which may possibly overlap with part or all of Farmer John's interval.
Please determine the total length of fence that is now covered with paint.

Input:

The first line of the input contains the integers a and b, separated by a space (a<b).
The second line contains integers c and d, separated by a space (c<d).
The values of a,b,c, and d all lie in the range 0…100, inclusive.

Output:

Please output a single line containing the total length of the fence covered with paint.
'''

ab = input()
cd = input()

a,b = map(int, ab.split())
c,d = map(int, cd.split())

if a<=c:
    diff1=c-a
else:
    diff1=a-c

if b<=d:
    diff2=d-b
else:
    diff2=b-d

if d<=b:
    Bob=b-a-diff2
else:
    Bob=b-a-diff1

if a<=c and d<=b:
    print(b-a)
elif c<=a and b<=d:
    print(d-c)
elif b<=c or d<=a:
    print(b-a+d-c)
else:
    print(diff1+Bob+diff2)
