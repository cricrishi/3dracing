import socket,thread,time
can_start={}
Y={}
H={}
X={}
S={}

class Server:
    def __init__(self):
        self.clients={}
        self.Y={}
        self.H={}
        self.X={}
        self.S={}
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
        i=0
        while True:
            conn,addr=s.accept()
            
            print 'connected to ',addr
            
            thread.start_new_thread(self.handleclient,(conn,i,))
            i=i+1

            
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
    def UpdateY(self,conn,i):
         global Y
         global H
         global X
         name=self.clients[i]
         l=str(conn.recv(2))
         l=int(l)
         self.Y[name]=str(conn.recv(l))
         print "Y updated "+self.Y[name]
         k=self.Y[name]
         Y=self.Y  
        # print "k is"+k
        # print "check"

    def UpdateS(self,conn,i):
         global S
         global Y
         global H
         global X
         name=self.clients[i]
         l=str(conn.recv(2))
         l=int(l)
         self.S[name]=str(conn.recv(l))
         print "S updated "+self.S[name]
         k=self.S[name]
         S=self.S  
        # print "k is"+k
        # print "check"


         
    def UpdateX(self,conn,i):
         global Y
         global H
         global X
         name=self.clients[i]
         l=str(conn.recv(2))
         l=int(l)
         self.X[name]=str(conn.recv(l))
         print "X updated "+self.X[name]
         k=self.X[name]
         X=self.X  
        # print "k is"+k
        # print "check"



    def UpdateH(self,conn,i):
         global Y
         global H
         global X
         
         name=self.clients[i]
         l=str(conn.recv(2))
         l=int(l)
         self.H[name]=str(conn.recv(l))
         print "H updated "+self.H[name]
         k=self.H[name]
         H=self.H
        # print "k is"+k
        # print "check"


    def recvH(self,conn,i):
        global Y
        global H
        global X
        try:
         print "sending"
     
         name=self.clients[i]

         print "sending..."
         print H
         print Y
         
         for i,j in H.items():
                if i!=name:
                   print "sending H "+str(i),str(name)
                   l=len(j) 
                   conn.send(b""+str(l))
                   conn.send(b""+str(j))
                 #  print "sending value of H "+str(j)
         for i,j in Y.items():
                if i!=name:
                   print "sending Y "+str(i),str(name)
                   l=len(j) 
                   conn.send(b""+str(l))
                   conn.send(b""+str(j))
                   print "sending value of Y "+str(j)

         for i,j in X.items():
                if i!=name:
                   print "sending X "+str(i),str(name)
                   l=len(j) 
                   conn.send(b""+str(l))
                   conn.send(b""+str(j))
                  # print "sending value of X "+str(j)


         for i,j in S.items():
                if i!=name:
                   print "sending X "+str(i),str(name)
                   l=len(j) 
                   conn.send(b""+str(l))
                   conn.send(b""+str(j))
                   print "sending value of S "+str(j)
        


        except Exception,e:
                print("error sending.."+str(e))



        
    def handleclient(self,conn,i):
        global can_start
        while True:
        

            try:
                
                data=conn.recv(7)
                if data:
                    print ("data recved is "+str(data))
                
                if str(data)=="pinging":
                    conn.send(b"active")
                    self.sendServerName(conn)

                if str(data)=="started":
                     

                     can_start[i]=1
                     chk=0
                    

                     for l,d in can_start.items():
                        if d==1:
                            chk=chk+1
                     if chk > 1:
                        conn.send(b"YES")
                     else:
                        conn.send(b"NOP")
                       
                        

                if str(data)=="connect":
                    
                    can_start[i]=0
                    global Y
                    global H
                    global X
                    global S
                    self.sendServerName(conn)
                    
                    cl=conn.recv(10)
                    self.clients[i]=str(cl)
                    self.tot=self.tot+1
                    cl=str(cl)
                    
                    
                    self.H[cl]="120.00000000000000000"
                    if i==0:
                      self.X[cl]="20.00000000000000"
                      self.Y[cl]="450.0000000000000000000000"
                    else:
                       self.X[cl]="50.00000000000000"
                       self.Y[cl]="430.0000000000000000000000"
                        
                    self.S[cl]="0.000000000000000000000000"
                    Y=self.Y
                    H=self.H
                    X=self.X
                    S=self.S

                    
                    print(cl+" joined the server")
                    

                    
                if str(data)=="request":
                    print ("requested")
                    self.clientRequest(conn)

                if str(data)=="sendedY":
            #        print ("Updating Y")
                    self.UpdateY(conn,i)

                if str(data)=="sendedX":
                    print ("Updating X")
                    self.UpdateX(conn,i)

                if str(data)=="sendedS":
                    print ("Updating S")
                    self.UpdateS(conn,i)
                


                if str(data)=="sendedH":
             #       print ("Updating H")
                    self.UpdateH(conn,i)


                if str(data)=="reicevH":

                    print ("get H")

                    self.recvH(conn,i)

                
            except Exception,e:
                print e
                break;

server=Server()
server.setServerName("Server2")
s=server.createServer()
server.monitorClients(s)

