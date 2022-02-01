# print pattern
def pattern(c='%',n=6,r=1):
    for i in range(r):
        print()
        for j in range(n):
            print(c,end='')
c=input(" enter a character:")
n=int(input(" enter a row element.."))
m=int(input(" enter the number of coloumns.."))
pattern()
pattern(c)
pattern(c,n)
pattern(c,n,m)
