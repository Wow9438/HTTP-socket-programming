					Assignment 2


# General:

From ES21BTECH11017_Assignment2.zip, copy basic and star folders and place them at /home/p4/tutorials/exercises

Since IP addresses of h1 (10.0.1.1), h2 (10.0.1.2) have fixed set of IP Addresses, so I had diectly fixed the IP's in client.py and server.py files in basic folder so that inorder to not enter IP Addresses for each and every request.

# Running the requests on the basic setup :

1. Open terminal, go to "/home/p4/tutorials/exercises/basic"
2. Run "make clean"
3. Run "make run"
4. You are now on the mininet prompt.
5. Run below commands to open the Host terminals:
	a. "xterm h1"
	b. "xterm h2"
6. Commands to run on h2's terminal
	a. bash h2-arp.sh (run once every time you run "make" above)
	b. python server.py
7. Command to run on h1's terminal
	a. bash h1-arp.sh (run once every time you run "make" above)
	b. python client.py
       		
Commands used below are to take request from h1's terminal.
       
		"PUT /assignment2/key1/val1 HTTP/1.1"
		"GET /assignment2?request=key1 HTTP/1.1"
		"DELETE /assignment2/key1 HTTP/1.1"


*Request should be enclosed quoted characters as shown above.

Since IP addresses of h1 (10.0.1.1), h2 (10.0.1.2), h3 (10.0.1.3) have fixed set of IP Addresses, so I had diectly fixed the IP's in client.py, cache.py and server.py files in star folder so that inorder to not enter IP Addresses for each and every request.


# Running the requests on the star setup :


1. Open terminal, go to "/home/p4/tutorials/exercises/star"
2. Run "make clean"
3. Run "make run"
4. You are now on the mininet prompt.
5. Run below commands to open the Host terminals:
	a. "xterm h1"
	b. "xterm h2"
	c. "xterm h3"
6. Commands to run on h2's terminal
	a. bash h2-arp.sh (run once every time you run "make" above)
	b. python cache.py
7. Commands to run on h3's terminal
	a. bash h3-arp.sh (run once every time you run "make" above)
	b. python server.py
8. Command to run on h1's terminal
	a. bash h1-arp.sh (run once every time you run "make" above)
	b. python client.py

Commands used below are to take request from h1's terminal.       		
       
		"PUT /assignment2/key1/val1 HTTP/1.1"
		"GET /assignment2?request=key1 HTTP/1.1"
		

*Request should be enclosed quoted characters as shown above.

and after each request , on h1's terminal whether connection is ok , bad or not found are also h1's terminal

connection is ok : "HTTPS/1.1 200 OK"
bad request  : "HTTPS/1.1 400 bad request"
Not Found : "HTTPS/1.1 404 Not Found"

*All timestamps are recorded from wireshark