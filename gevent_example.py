
import gevent
from gevent import socket
hosts = ['www.crappytaxidermy.com', 'www.sina.com.cn','www.sohu.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
