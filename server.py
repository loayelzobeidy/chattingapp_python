import thread
import socket
names = []
sockets = []
def recievemess(threadname,socket):
	while 1:
		index = -1
		message = socket.recv(1024)
		array=message.split(":",2)
		recievername = array[0]
		message1 = array[1]
		for i,name in enumerate(names):
			if name==recievername :
				index = i
		if(index ==-1) :
			smaster.send(message)
			print ("not found")
		sockets[index].send(message)
		
    
        
 
       #c.close()

s = socket.socket() #Create a socket object
host = socket.gethostname() #Get the local machine name
port = 14000 # Reserve a port for your service
portmaster = 13002 # reserverd for the master server
smaster = socket.socket()
#smaster.bind((host,portmaster))
s.bind((host,port)) #Bind to the port
smaster.connect((host,portmaster))
mastermessage = smaster.recv(1024)
print mastermessage
sockets=[]
s.listen(5) #Wait for the client connection
while True:
        
        c,addr = s.accept()
        sockets.append(c)
         #Establish a connection with the client
        print "Got connection from", addr
        c.send("Thank you for connecting!")
        name =c.recv(1024)
        print name+"Logged In"
        names.append(name)
        thread.start_new_thread(recievemess,("Thread1",c))
        thread.start_new_thread(recievemess,("Thread2",smaster))

while 1:
   pass