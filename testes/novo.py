a,b,c,d = input().split()

A = int(a)
B = int(b)
C = int(c)
D = int(d)

if B > C:
    if D > A:
        if C+D > A+B:
            if C > 0:
                if D > 0:
                    if A % 2 == 0:
                        print('Valores aceitos')
else:
    print('Valores nao aceitos')