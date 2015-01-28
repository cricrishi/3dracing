import socket,thread

class Server:
    def __init__(self):
        self.clients={}
        self.Y={}
        self.H={}
        self.tot=0
        self.name="S1"
        self.port=50007
        self.host=socket.gethostbyname(socket.gethostname())
    def createServer(self):
        s=socket.socket()
        s.bind((self.host,self.port))
        s.listen(5)
        return s
    def setServerName(self,name):
        self.name=name

    def sendServerName(self,conn):
        conn.send(b""+self.name)
        
    def monitorClients(self,s):
        while True:
            conn,addr=s.accept()
            print 'connected to ',addr
            thread.start_new_thread(self.handleclient,(conn,))

            
    def clientRequest(self,conn):
        while True:
            req=str(conn.recv(12))

            if req=="getplayers":
                print "requested players"
                for k, v in self.clients.iteritems():
                    l=len(str(v))
                    conn.send(b""+str(l))
                    conn.send(b""+str(v))

            if req=="getcount":
                print "requested total players"
                conn.send(b""+str(self.tot))

            if req=="exit":
                print "exiting request mode"
                return
    def UpdateY(self,conn):
         l=str(conn.recv(1))
         l=int(l)
         name=str(conn.recv(l))
         l=str(conn.recv(2))
         l=int(l)
         self.Y[name]=str(conn.recv(l))
         print "Y updated "+self.Y[name]
         k=self.Y[name]
  
         print "k is"+k
         print "check"
         
    def UpdateH(self,conn):
         l=str(conn.recv(1))
         l=int(l)
         name=str(conn.recv(l))
         l=str(conn.recv(2))
         l=int(l)
         self.H[name]=str(conn.recv(l))
         print "H updated "+self.H[name]
         k=self.H[name]
         print "k is"+k
         print "check"

    def recvY(self,conn):
        
          l=str(conn.recv(1))
          l=int(l)
          name=str(conn.recv(l))
          for i,j in self.Y.items():
             if i!=name:
                print i,name
                l=len(j) 
                conn.send(b""+str(l))
                conn.send(b""+str(j))

    def recvH(self,conn):
        try:
         l=str(conn.recv(1))
         l=int(l)
         name=str(conn.recv(l))
         
         while 1:
            print "sending..."
            for i,j in self.H.items():
                if i!=name:
                   print i,name
                   l=len(j) 
                   conn.send(b""+str(l))
                   conn.send(b""+str(j))
            for i,j in self.Y.items():
                if i!=name:
                   print i,name
                   l=len(j) 
                   conn.send(b""+str(l))
                   conn.send(b""+str(j))
        except Exception,e:
                print("error sending.."+str(e))



        
    def handleclient(self,conn):
        while True:
        

            try:
                
                data=conn.recv(7)
                if data:
                    print (str(data))
                
                if str(data)=="pinging":
                    conn.send(b"active")
                    self.sendServerName(conn)
                    
                if str(data)=="connect":
                    self.sendServerName(conn)
                    
                    cl=conn.recv(10)
                    self.clients[self.tot]=str(cl)
                    self.tot=self.tot+1
                    cl=str(cl)
                    self.Y[cl]="380"
                    self.H[cl]="2"
                    
                    print(cl+" joined the server")
                    
                if str(data)=="request":
                    print ("requested")
                    self.clientRequest(conn)

                if str(data)=="sendedY":
                    print ("Updating Y")
                    self.UpdateY(conn)


                if str(data)=="sendedH":
                    print ("Updating H")
                    self.UpdateH(conn)

                if str(data)=="reicevY":

                    print ("get Y")
                    self.recvY(conn)

                if str(data)=="reicevH":

                    print ("get H")

                    thread.start_new_thread(self.recvH,(conn,))

                
            except Exception,e:
                pass

server=Server()
server.setServerName("Server2")
s=server.createServer()
server.monitorClients(s)

