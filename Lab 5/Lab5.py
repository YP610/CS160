import math
import time



def iterations():
    x=[]
    j=0
    start_time=time.time()
    while(j<10):
        x.insert(0,int(input("Enter number ")))
        j+=1
    cpu_time=time.process_time()
    end_time=time.time()
    
    print(f"it took {end_time - start_time} seconds to iterate 10 times and the cpu time is {cpu_time}")




import math
import time
start_time = time.time()
x = math.sqrt(3.14159)
end_time = time.time()
print("the computation took ", end_time - start_time, " seconds.")

iterations()