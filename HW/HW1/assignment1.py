def is_prime(num):
    counter=0
    for i in range(2,num,1):
        if num%i==0:
            counter+=1
        
    if counter>0:
        return False
    
    return True
    

def are_relatively_prime(num1, num2):

    list1=[]
    list2=[]
    
    if num2%num1==0 or num1%num2==0:
        return False
    for i in range(2,num1,1):
        if num1%i==0:
            list1.append(i)
    
    for j in range(2,num2,1):
            if num2%j==0:
                list2.append(j)
    
    for i in list1:
        for j in list2:
            if i==j:
                return False
     
    return True
        

def primes(nums):
    x=[]
    y=nums
    
    for i in range(2,nums+1,1):
        if is_prime(i)==True:
            x.append(i)
    return x
    
   


def prime_decomposition(num):
    x=primes(num)
    y=[]

    while num!=1:
        for i in x:
            if num%i==0:
                y.append(i)
                num/=i
        
    return y

    
def has_prime_decomposition_of_size_2_and_factors_are_different(num):
    x=prime_decomposition(num)
    if len(x)==2:
        if x[0]!=x[1]:
            return True
    return False
        
        
        
