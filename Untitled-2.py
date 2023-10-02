QA = 30

Y = ['b', 'd', 'f']
y = ['10', '10', '30']

A = ['a', 'c', 'e']
a = ['25', '10', '40']


g = len(a)+1
h = len(y)+1
e = 0
f = 0
k = 0
j = 0
m = 0
n = 0
if len(a)>=len(y):
    for n in range(len(a)):
        if f < g:
            d = int(a[f])
            e = e+d
            print(str(e) +'h')
            if e > QA and f+k != 0:
                print('break')
                e = 0
            else:
                print(d)
            f = f+1
        
        if k < h:
            d = int(y[k])
            e = e+d
            print(str(e)+'h')
            if e > QA and f+k != 0:
                print('break')
                e = 0
            else:
                print(d)
            k = k+1

if len(y)>len(a):
    for n in range(len(y)):
        if f < g:
            d = int(a[f])
            e = e+d
            if e > QA and f+k != 0:
                print('break')
                e = 0
            else:
                print(d)
            f = f+1
        
        if k < h:
            d = int(y[k])
            e = e+d
            if e > QA and f+k != 0:
                print('break')
                e = 0
            else:
                print(d)
            k = k+1
