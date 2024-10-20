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