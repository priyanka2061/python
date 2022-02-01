# find fibonacci series usinf recursion
def fibo( n):
    if(n<2):
       return 1
    return(fibo(n-1)+fibo(n-2))
n=int(input(" enter a number"))
for i in range(n):
    print(" fibonaccci",fibo(i))

   



