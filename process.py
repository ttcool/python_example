#!/usr/bin/python  
#-*-coding:utf-8-*-  
      
import threading
def counter(n):  
    cnt = 0;  
    for i in xrange(n):  
        for j in xrange(i):  
            cnt += j;  
        print cnt;              
                  
if __name__ == '__main__':  
    th = threading.Thread(target=counter, args=(10,));  
    th.start();  
    th.join();  
