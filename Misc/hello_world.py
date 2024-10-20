import math

def practice(c,p):
    h=c[0]
    k=c[1]
    r=c[2]
    pt=p[0]
    pt2=p[1]
    if(math.sqrt((h-pt)**2+(k-pt2**2)<=r)):
        return True

    return False




def practice2(circle,listOfPoints):
    for i in listOfPoints:
        if practice(circle,i)==False:
            return i
    return -1


def list_custom_average(a):
    neg=[]
    sum=0
    count=0
    for i in range(len(a)):
        if a[i]>=0:
            sum+=a[i]
            count+=1
        elif a[i]<0:
            neg.append(i)
    if sum==0:
        return None
    elif len(neg)>0:
        return neg, sum/count
    
    
    else:
        return sum/count
    
def search(lis, low, high):
    empty=[]
    currNum=0
    result=0
    for i in lis:
        j=i
        j*=10
        j%=10
        num=int(j)
        if num>=low and num<= high:
            if i>result:
                if num>currNum:
                    currNum=i
                    result=i
    if result==0:
        return empty
    return result

z=[1.54,0.56,1.73333,4.578]
print(search(z,3,9))

j=12.34
i=j
j/=10
i%=10
print(i,j)