def answer(a):
	
    x=[]
   
    i=0
    j=len(a)-1
    while i<len(a) and j>=0 and i<j:
        x.append(a[i])
        x.append(a[j])
        i+=1
        j-=1

    if len(a)%2!=0:
        c=len(a)//2
        x.append(a[c])
        
    return x


# dont modify this code unless you know what you are doing
t = int(input())
while(t):
	t -= 1
	n = int(input()) # this is the number of elements in the sequence
	a = [int(i) for i in input().split()] # this is the sequence you need to work on
	print(*answer(a));







