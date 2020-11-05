#starFormation1 (4)

def starFormation1 (n):
    i = 0
    while (i < n):
        i += 1
        print('* ' * i)
starFormation1 (4)
print()


#starFormation2 (4)
def starFormation2 (n):
    i = 0
    print ('* ' * n)
    while (n > 0):
        n-= 1
        print('* ' * n)
starFormation2 (4)
print()


#starFormation3 (7)
def starFormation3 (n):
    i = 0
    while (i < 4):
        i += 1
        print('* ' * i)
    i = 4
    while (i > 1):
        i -= 1
        print('* ' * i)
starFormation3 (7)
print()
