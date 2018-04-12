#!usr/bin/env python3
# -*- codeing:utf-8 -*-

import sys
import getopt
import socket

def getargvs(argv):
    argvs, argvopts = getopt.getopt(argv, '',['host=', 'port='])
    for arg_name, arg_value in argvs:
        if arg_name in ['--host']:
            host = arg_value
        if arg_name in ['--port']:
            port = arg_value
  
    ports = []

    if len(host.split('.')) != 4:
        print('Parameter Error')
        exit()
    else:
        for a in host.split('.'):
            try: int(a)
            except:
                print('Parameter Error')
                exit()

    try:
        if '-' in port:
            min_, max_ = tuple(port.split('-'))
            min_ = int(min_)
            max_ = int(max_)
            while min_ <= max_:
                ports.append(min_)
                min_ += 1
        else:
            ports=[int(port)]

        return host, ports

    except:
        print("Parameter Error")
        exit()
   

def verify(host, ports):
    
    s = socket.socket()
    s.settimeout(0.1)
    for port in ports:
        try:
            s.connect((host, port))
            print(str(port)+' '+'open')
        except:
            print(str(port)+' '+'closed')
    s.close()

if __name__ == '__main__':

    host, ports = getargvs(sys.argv[1:])
    verify(host, ports)

