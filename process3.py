import threading, time, random  
      
def counter():  
    cnt = 0;  
    for i in xrange(10000):  
        for j in xrange(i):  
            cnt += j;  
      
class SubThread(threading.Thread):  
    def __init__(self, name):  
        threading.Thread.__init__(self, name=name);  
      
    def run(self):  
        i = 0;  
        while i < 4:  
            print self.name,'counting...\n';  
            counter();  
            print self.name,'finish\n';  
            i += 1;  
      
if __name__ == '__main__':  
      
    th = SubThread('thread-1');  
    th.start();  
    th.join();  
    print 'all done';  
