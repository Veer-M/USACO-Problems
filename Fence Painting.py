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