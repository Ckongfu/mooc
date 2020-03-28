import time

for i in range(101):
    print('\r{:^6}%'.format(i),end='')
    time.sleep(0.01)

