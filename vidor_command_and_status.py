import socket
import sys
import keyboard
from thread import *

HOST = ''   
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Receving Data...\n') 
    f=open('out.txt','w')
    #infinite loop so that function do not terminate and thread do not end.
    while True:
	    if keyboard.is_pressed('0'):
        conn.send('0')
        print "sending 0"
      elif 
        
      
      #Receiving from client
      data = conn.recv(1024)
      if not data:
        break
	    f.write(data)
    conn.close()

#now keep talking with the client
while 1:
    #wait to accept a connection
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread
    start_new_thread(clientthread ,(conn,))

s.close()

