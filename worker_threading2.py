#coding=utf-8
import threading
from time import ctime,sleep


def music(func):
    print "I was listening to %s. %s" %(func,ctime())
    sleep(1)

def move(func):
    print "I was at the %s. %s" %(func,ctime())
    sleep(5)

threads = []
[threads.append(threading.Thread(target=music,args='a')) for x in range(8)]
[threads.append(threading.Thread(target=move,args='b')) for x in range(8)]

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

    print "all over %s" %ctime()
