import time
def wait():
    time.sleep(5)

star=time.perf_counter()
a=0
for i in range(101):
    a+=i
print (a)
wait()
end=time.perf_counter()
Time=end-star
print()
print(Time)
