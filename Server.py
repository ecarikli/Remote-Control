import socket
from string import ascii_letters
from threading import Thread
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("0.0.0.0", 2222) )
s.listen()
conn, addr = s.accept()

def key_word(data):
    tWord = "x"
    data = len(data)
    for x in range(data-1):
        tLetter = random.choice(ascii_letters)
        tWord += tLetter
    return tWord

def xor(operand1, operand2):
    byte1 = operand1.encode()
    byte2 = operand2.encode()
    length = len(operand1)
    xored = []
    for i in range(length):
        xor_result = byte1[i] ^ byte2[i]
        xored.append(xor_result)
    xored = bytes(xored)
    return xored

def listen(s):
    while True:
        data = s.recv(10000000000)
        data = data.decode("utf-8", "ignore")
        if data[0] == "x":
            print("The key is:", data,"\n")
        else:
            print(data)

def send(s):
    while True:
        data = input("") + "\n"
        tKey = key_word(data)
        tMessage = xor(data, tKey)
        tKey = tKey.encode()
        s.send(tMessage)
        s.send(tKey)

Thread(target=listen, args=(conn,)).start()
Thread(target=send, args=(conn,)).start()
