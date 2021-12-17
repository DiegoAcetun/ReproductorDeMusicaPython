import threading
import time
import datetime
def a():
    time.sleep(5)
    print('hola')
t1 = threading.Thread(name='hilo1', target=a)
# t1.start()
tiempo = 5
i=0
while i<=tiempo:
    print(i)
    i+=1
    time.sleep(1)
