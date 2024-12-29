def primeseive(n):
    prime=[True for i in range(n+1)]
    currentnum=2
    while(currentnum*currentnum<=n):
        if(prime[currentnum]==True):
            for i in range(currentnum**2,n+1,currentnum):
                prime[i]=False
        currentnum+=1
    prime[0]=False
    prime[1]=False
    for p in range(n+1):
        if prime[p]:
            print(p)
n=int(input("Enter number to find all prime numbers less that the number: "))
primeseive(n)
print("Following are the prime numbers smaller.")
print("than or equal to")