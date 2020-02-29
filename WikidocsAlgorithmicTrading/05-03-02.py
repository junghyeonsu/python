import time

print(time.time())
print(time.ctime())

thisTime = time.ctime().split(' ')[3]
print(thisTime)

# for i in range(10):
#     print(time.ctime().split(' ')[3])
#     time.sleep(1)

print(dir(time))