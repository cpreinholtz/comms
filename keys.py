from thread import *
import socket
import sys
import time
import keyboard
#
import keys







#filename="./out/output_"+time.ctime()+".txt"
#filename=filename.replace(" ","_")


def send_key(conn):
  control="khtcof0123456789"  
  pressed=False
  for c in control:
    if keyboard.is_pressed(c):
    
      print("sending:" +c)
      conn.send(key)
      return True
      
  return False
      




def clientthread(conn):
  conn.send('Welcome to the server. Receving Data...\n') 
  print "Entering Loop..."

  while True:
    try:
      send_key(conn)
      time.sleep(0.2)
      
      
    except:
      conn.close()
      print("dieing")
      exit()
  conn.close()
  print "Connection Closed"
  
  
  
  
  
  
  
  
def start_socket():
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
  return s




