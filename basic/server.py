import socket

#WRITE CODE HERE:
#1. Create a KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).
keyvalue_pairs = {
            '1' : '500',
            '2' : '50',
            '3'   : '551',
            '4' : '500',
            '5' : '50',
            '6'   : '551'

}

#dst_ip = str(input('Enter Server IP: '))

s = socket.socket()
#print ('Socket successfully created')#written by me

dport = 12346

s.bind(("10.0.1.2", dport))
print ('socket binded to %s' %(dport))

s.listen(5)
#print ('socket is listening')#written by me

while True:
  c, addr = s.accept()
  print ('Got connection from', addr )
  #recvmsg = c.recv(1024).decode()
  #print('Server received '+recvmsg)
  #c.send('Hello client'.encode())

  #Write your code here
  #1. Uncomment c.send
  #2. Parse the received HTTP request
  #3. Do the necessary operation depending upon whether it is GET, PUT or DELETE
  #4. Send response
  ##################
  recvmsg = c.recv(1024).decode()
  z = 0
  for i in recvmsg:
      if(i=='/'):
         z = z+1
  if (recvmsg[0:25] == 'GET /assignment2?request=' and z==2 and len(recvmsg)-8 > 25 and recvmsg[len(recvmsg)-8:len(recvmsg)] == 'HTTP/1.1') :
      for i in range(25,len(recvmsg)):
          if(recvmsg[i] == ' '):
              j = i
              break
      key = recvmsg[25:j]
      if key in keyvalue_pairs:
          c.send('HTTP/1.1 200 OK '.encode())
          c.send(keyvalue_pairs[key].encode())
      else :
          c.send('HTTP/1.1 404 NOT FOUND'.encode())
  elif (recvmsg[0:17] == 'PUT /assignment2/' and z==4 and len(recvmsg)-8 > 17 and recvmsg[len(recvmsg)-8:len(recvmsg)] == 'HTTP/1.1') :
      for i in range(17,len(recvmsg)):
          if(recvmsg[i] == '/') :
              j = i
              break
      key = recvmsg[17:j]
    #   for i in range(j+1,len(recvmsg)):
    #       if(recvmsg[i] == ' ') :
    #           k = i
    #           break
      value = recvmsg[j+1:len(recvmsg)-9]
      if key in keyvalue_pairs :
          keyvalue_pairs[key] = value
          c.send('HTTP/1.1 200 OK '.encode())
          c.send('updated'.encode())
      else :
          keyvalue_pairs[key] = value
          c.send('HTTP/1.1 200 OK '.encode())
          c.send('added'.encode())
  elif (recvmsg[0:20] == 'DELETE /assignment2/' and z==3 and len(recvmsg)-8 > 20 and recvmsg[len(recvmsg)-8:len(recvmsg)] == 'HTTP/1.1'):
       for i in range(20,len(recvmsg)):
           if(recvmsg[i] == ' ') :
               j = i
               break
       key = recvmsg[20:j]
       if key in keyvalue_pairs:
           del keyvalue_pairs[key]
           c.send('HTTP/1.1 200 OK '.encode())
           c.send('deleted'.encode())
       else :
           c.send('HTTP/1.1 404 Not Found'.encode())
  else :
      c.send('HTTP/1.1 400 bad request'.encode())
  c.close()
  #break
