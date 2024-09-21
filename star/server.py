import socket

server_ip ='10.0.1.3'
cache_ip = '10.0.1.2'
server_port = 12345
cache_port=11017
print('server')
key_valuepairs = {
    '1' : '100',
    '2' : '200',
    '3' : '300',
    '4' : '400',
    '5' : '500',
    '6' : '600'
}

server = socket.socket()
server.bind((server_ip,server_port))
server.listen(5)
print('server listening')#######
while True :
    cache,addr = server.accept()
    print("got connection from ",addr)
    recvd_msg1 = cache.recv(1024).decode()
    z = 0

    for i in recvd_msg1:
         if(i=='/'):
            z = z+1
    if (recvd_msg1[0:25] == 'GET /assignment2?request=' and z==2 and len(recvd_msg1)-8 > 25 and recvd_msg1[len(recvd_msg1)-8:len(recvd_msg1)] == 'HTTP/1.1') :
        key = recvd_msg1[25:len(recvd_msg1)-9]
        if key in key_valuepairs:
            cache.send('HTTP/1.1 200 OK '.encode())
            cache.send(str(key_valuepairs[key]).encode())
        else :
            cache.send('HTTP/1.1 404 Not Found'.encode())
    elif (recvd_msg1[0:17] == 'PUT /assignment2/' and z==4 and len(recvd_msg1)-8 > 17 and recvd_msg1[len(recvd_msg1)-8:len(recvd_msg1)] == 'HTTP/1.1'):
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
        if key in key_valuepairs :
            cache.send('HTTP/1.1 200 OK '.encode())
            cache.send('updated'.encode())
        else :
            cache.send('HTTP/1.1 200 OK '.encode())
            cache.send('added'.encode())
        key_valuepairs[key] = value

    else :
        cache.send('HTTP/1.1 400 bad request'.encode())
    cache.close()
