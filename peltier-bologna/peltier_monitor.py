#!/usr/bin/env python3

import socket
import time
import sys
import signal

loop_forever = True
def sigterm_handler(_signo, _stack_frame):
    global loop_forever
    loop_forever = False

signal.signal(signal.SIGTERM, sigterm_handler)
signal.signal(signal.SIGINT, sigterm_handler)

SOCKTSX = '/tmp/tsx1820p_server.socket'
SOCKARD = '/tmp/arduino_server.socket'
SOCKML = ['/tmp/masterlogic_server.ML' + str(x) + '.socket' for x in range(0,4)]

_tsta = 0
_vset = 0
_vout = 0
_iset = 0
_iout = 0
_temp = [0, 0, 0, 0]

while loop_forever:

    tsta = time.time()

    ### TSX power supply
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.connect(SOCKTSX)
        
        ### vset
        s.sendall(b'V1?')
        vset = s.recv(1024).decode()
        vset = vset.split()[1]
        ### vout
        s.sendall(b'V1O?')
        vout = s.recv(1024).decode()
        vout = vout[:-1]
        ### iset
        s.sendall(b'I1?')
        iset = s.recv(1024).decode()
        iset = iset.split()[1]
        ### iout
        s.sendall(b'I1O?')
        iout = s.recv(1024).decode()
        iout = iout[:-1]

    ### masterlogic boards
    temp = [0, 0, 0, 0]
    for ml in range(0,4):
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
            s.connect(SOCKML[ml])
            s.sendall(b'L')
            temp[ml] = s.recv(1024).decode().split()[2]
            
    ### arduino
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.connect(SOCKARD)
        s.sendall(b'temp')
        tempin = s.recv(1024).decode()
        s.sendall(b'rh')
        rhin = s.recv(1024).decode()
            
    print(tsta, vset, vout, iset, iout, temp[0], temp[1], temp[2], temp[3], tempin, rhin)
    sys.stdout.flush()
            
    time.sleep(1)
