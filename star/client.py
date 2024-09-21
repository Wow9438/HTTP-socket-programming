import socket

server_ip='10.0.1.3'
cache_ip='10.0.1.2'
cache_port = 11017
server_port = 12345
print('client')
client = socket.socket()

request_from_client = str(input('Enter the request : '))
#request_from_client = 'GET /assignment2?request=1 HTTP/1.1'
#request_from_client = 'PUT /assignment2/66/10 HTTP/1.1'
#
# request_from_client = ('GET /assignment2?request=5 HTTP/1.1')
# if (request_from_client[0] =='1'):
#     #get request
#     client.connect((cache_ip,cache_port))
#     client.send(request_from_client.encode())
#     value = client.recv(1024).decode()
#     print(value)
# elif (request_from_client[0] == '2'):
#     client.connect((server_ip,server_port))
#     client.send(request_from_client.encode())
#     recvd_msg_cache = client.recv(1024).decode()
#     print(recvd_msg_cache)
# else :
client.connect((cache_ip,cache_port))
client.send(request_from_client.encode())
recvd_msg_cache = client.recv(1024).decode()
print(str(recvd_msg_cache))

if(recvd_msg_cache == 'HTTP/1.1 200 OK '):
    recv_from_cache = client.recv(1024).decode()

    print('\n{'+str(recv_from_cache)+'}')


client.close()
