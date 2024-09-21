import socket

serverIP = '10.0.1.2'

#dst_ip = str(input('Enter dstIP: '))
s = socket.socket()

print(serverIP)

port = 12346
#print('socket connection intialized')#written by me
s.connect((serverIP, port))

#Write your code here:
#1. Add code to send HTTP GET / PUT / DELETE request. The request should also include KEY.
#2. Add the code to parse the response you get from the server.


req_from_client = str(input('Enter the request :'))
#req_from_client = "GET /assignment2?request=1 HTTP/1.1"
#req_from_client = "PUT /assignment2/3/10 HTTP/1.1"
#req_from_client = "DELETE /assignment2/6 HTTP/1.1"
#s.send('Hello server'.encode())
#print ('Client received '+s.recv(1024).decode())
s.send(req_from_client.encode())#--------------------#
response = s.recv(1024).decode()
print(response)
if (response =='HTTP/1.1 200 OK ') :
    msg_from_server = s.recv(1024).decode()
    print("\n{"+msg_from_server+"}")#-----------#
# print('socket closes')#written by me
s.close()
