summ=0
n=5
arr=[10,11,7,12,14]
for i in range(0,len(arr)-1):
    temp=abs(arr[i+1]-arr[i])
    summ += temp
print(summ)
 
  
