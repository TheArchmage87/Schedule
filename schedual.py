print("hi")
QA = input('About how long do you want your work peiriods to be?')
QA = int(QA)

Y = []
y = []
x = input('How many subjects do you need to study for?')
x = int(x)
for i in range(x):
    Z = input('Which subjects are you studying?')
    Y.append(Z)
    z = input('For how long?')
    y.append(z)

A = []
a = []
c = input('How many classes homework do have to do?')
c = int(c)
for i in range(c):
    B = input('What homework do you have?')
    A.append(B)
    b = input('How long will it take?')
    a.append(b)

g = len(a)+1
h = len(y)+1
e = 0
f = 0
k = 0
j = 0
if len(a)>len(y):
    for n in range(len[y]):
        if f < g:
            d = int(a[f])
            e = e+d
            if e <= QA or e > QA and f+k == 0:
                j = e
            else:
                m = 0
                n = 0
                for l in range(k):
                    if n == 0:
                        print(A[m])
                    if n == 1:
                        print(Y[m])
                        m = m+1
                        n = 0
                    else:
                        n = 1

            f = f+1
        
        if k < h:
            d = int(y[k])
            e = e+d
            if e <= QA or e > QA and f+k == 0:
                j = e
            else:
                m = 0
                n = 0
                for l in range(k):
                    if n == 0:
                        print(A[m])
                    if n == 1:
                        print(Y[m])
                        m = m+1
                        n = 0
                    else:
                        n = 1

            k = k+1

if len(y)>len(a):
    for n in range(len[y]):
        if f < g:
            d = int(a[f])
            e = e+d
            if e <= QA or e > QA and f+k == 0:
                j = e
            else:
                m = 0
                n = 0
                for l in range(k):
                    if n == 0:
                        print(A[m])
                    if n == 1:
                        print(Y[m])
                        m = m+1
                        n = 0
                    else:
                        n = 1

            f = f+1
        
        if k < h:
            d = int(y[k])
            e = e+d
            if e <= QA or e > QA and f+k == 0:
                j = e
            else:
                m = 0
                n = 0
                for l in range(k):
                    if n == 0:
                        print(A[m])
                    if n == 1:
                        print(Y[m])
                        m = m+1
                        n = 0
                    else:
                        n = 1

            k = k+1
