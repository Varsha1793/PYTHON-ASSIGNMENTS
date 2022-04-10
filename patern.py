# TRIANGLE 1
x = 5
i = 0
while i <= x - 1:
    j = 0
    while j < i:
        print('', end=' ')
        j =j+ 1
    k = i
    while k <= x - 1:
        print('*', end=' ')
        k += 1
    print()
    i=i+1

# TRIANGLE 2
i = x - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= x - 1:
        print('*', end=' ')
        k=k+1
    print('')
    i=i-1
