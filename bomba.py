import time
import sys

i = int(sys.argv[1])
while i > 0:
    print(i)
    time .sleep(1) #espera 1 segundo 
    i -= 1
    #i =i - 1
print("BOOM!!") 
