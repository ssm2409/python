def calcTotalTax(arr,n):
    k=[]
    for i in arr:
        if(i>=100):
            f=int(.1*(i-100)+i)
            k.append(f)
        else:
            f=int(i)
            k.append(f)
    print(sum(k)-sum(arr))
n=int(input())
arr=list(map(int,input().split()))
calcTotalTax(arr,n)
