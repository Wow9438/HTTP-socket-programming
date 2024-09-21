import socket

server_ip = '10.0.1.3'
cache_ip = '10.0.1.2'
cache_port=11017
server_port = 12345
print('cache')
key_valuepairs = {

}

cache = socket.socket()
cache.bind((cache_ip,cache_port))
cache.listen(5)
print('cache listening')########
while True :
    client, addr = cache.accept()
    print("got connection from ",addr)
    recvd_msg1 = client.recv(1024).decode()
    z = 0
    for i in recvd_msg1:
        if(i=='/'):
            z = z+1
    if (recvd_msg1[0:25] == 'GET /assignment2?request=' and z==2 and len(recvd_msg1)-8 > 25 and recvd_msg1[len(recvd_msg1)-8:len(recvd_msg1)] == 'HTTP/1.1') :
        key = recvd_msg1[25:len(recvd_msg1)-9]
        if key in key_valuepairs:
            client.send('HTTP/1.1 200 OK '.encode())
            client.send(str(key_valuepairs[key]).encode())
        else :
            cache1 = socket.socket()
            cache1.connect((server_ip,server_port))
            cache1.send(recvd_msg1.encode())
            recvd_msg2 = cache1.recv(1024).decode()
            if(recvd_msg2 == 'HTTP/1.1 200 OK '):
                recvd_server = cache1.recv(1024).decode()
                key_valuepairs[key] = recvd_server
                client.send(recvd_msg2.encode())
                client.send(recvd_server.encode())
            else:
                client.send(recvd_msg2.encode())
            cache1.close()
    elif (recvd_msg1[0:17] == 'PUT /assignment2/' and z==4 and len(recvd_msg1)-8 > 17 and recvd_msg1[len(recvd_msg1)-8:len(recvd_msg1)] == 'HTTP/1.1') :
        cache1 = socket.socket()
        for i in range(17,len(recvd_msg1)):
          if(recvd_msg1[i] == '/') :
              j = i
              break
        key = recvd_msg1[17:j]
        # for i in range(j+1,len(recvd_msg1)):
        #     if(recvd_msg1[i] == ' ') :
        #         k = i
        #         break
        value = recvd_msg1[j+1:len(recvd_msg1)-9]
        if key in key_valuepairs:
            key_valuepairs[key] = value
        cache1.connect((server_ip,server_port))
        cache1.send(recvd_msg1.encode())
        msg_from_server = cache1.recv(1024).decode()
        client.send(msg_from_server.encode())
        msg_server2 = cache1.recv(1024).decode()
        client.send(msg_server2.encode())
        cache1.close()
    else :
        cache1 = socket.socket()
        cache1.connect((server_ip,server_port))
        cache1.send(recvd_msg1.encode())
        msg_from_server = cache1.recv(1024).decode()
        client.send(msg_from_server.encode())
        cache1.close()
    client.close()
