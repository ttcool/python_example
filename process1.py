#!/usr/bin/python

#-*-coding:utf-8-*-



import threading

class Callable(object):

    def __init__(self, func, args):

        self.func = func;

        self.args = args;

    def __call__(self):

        apply(self.func, self.args);



def counter(n):

    cnt = 0;

    for i in xrange(n):

        for j in xrange(i):

            cnt += j;

    print cnt;



if __name__ == '__main__':

    th = threading.Thread(target=Callable(counter, (1000,)));

    th.start();

    th.join();
