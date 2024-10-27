def change_given(cost,amount,bills):
    change=amount-cost
    result=[]
    for i in bills:
        count=0
        while(change>=i):
            change-=i
            count+=1
        result.append(count)
    return result
 
 
a=[20,10,5,2,1]   
print(change_given(47,200,a))

x=[]

print(len(x))

def search(target,x):
    
    mid=(len(x)-1)//2
    
    while(target!=x[mid]):
        if target>x[mid]:
            mid+=1
        else:
            mid-=1
    
    return mid

x=[2,4,6,7,8,9]

print(search(9,x))

def duplicatePairs(arr):
    count=0
    for i in range(0,(len(arr))-2):
        if arr[i]==arr[i+1]:
            count+=1
    return len(arr)

a=[1,2,2,5,6,7,3,3,5,7,5,5,7,8,4,4,8,9,9]
print(duplicatePairs(a))
    
    