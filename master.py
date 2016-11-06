import socket
import thread
def recievemess(threadname,currentindex,socket):
	while 1:
		index = -1
		message = socket.recv(1024)
		servers[(currentindex+1)%(len(servers))].send(message)
		print ("sent")
		
    
s=socket.socket()
host = socket.gethostname()
portmaster = 13002
s.bind((host,portmaster))
s.listen(5)
servers =[]
index = 0
while True:
        
        c,addr = s.accept()
        servers.append(c)
        index+=1
         #Establish a connection with the client
        print "Got connection from", addr
        c.send("Thank you for connecting!")
        thread.start_new_thread(recievemess,("Thread1",index,c))
while 1 :
	pass

