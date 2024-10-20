def answer(a):
    x=[]
    i=0
    j=len(a)-1     
    while i<=j:
        x.append(a[i])
        if(i!=j):
            x.append(a[j])
        i+=1
        j-=1    
    return x


# dont modify this code unless you know what you are doing
t = int(input())
while(t):
	t -= 1
	n = int(input()) # this is the number of elements in the sequence
	a = [int(i) for i in input().split()] # this is the sequence you need to work on
	print(*answer(a))
 
def answer(s):
    length=len(s)
    i=0
    j=len(s)-1
    while(((s[i]=="0"and s[j]=="1") or (s[i]=="1" and s[j]=="0")) and i<j):
        length-=2
        i+=1
        j-=1  
    return length


# dont modify this code unless you know what you are doing
t = int(input())
while(t):
	t -= 1
	n = int(input()) # this is the length of the input string
	s = input() # this is the string you need to work on
	print(answer(s))







