import thread
import socket

class Client:
    def __init__(self):
        self.port=50007
        self.name="parag"
        self.servers={}
        self.s=socket.socket()
        
    def iptol(self,ip):
        return ip.split('.')
    def ltoip(self,l):
        return l[0]+'.'+l[1]+'.'+l[2]+'.'+l[3]
    def giveip(self,ip):
        for j in range(256):
            ip1=self.iptol(ip)
            ip1[3]=str(j)
            k=self.ltoip(ip1)            
            thread.start_new_thread(self.check,(k,))
        
    def getip(self):
        return socket.gethostbyname(socket.gethostname())
    
    def check(self,host):
        try:
            s=socket.socket()
            s.connect((host,self.port))
            s.send(b"pinging")
            
            print ("pinged")
            l=s.recv(6)

            if(str(l)=="active"):
                print ("host is "+host)
                name=s.recv(7)
                self.servers[host]=name
                
                print (name)
                s.close()
        except Exception,e:
            pass
    def connectServer(self,host):
        try:
            s=socket.socket()
            s.connect((host,self.port))
            s.send(b"connect")
            name=s.recv(10)
            print("connected to "+name)
            s.send(b""+self.name)
        
            self.s=s
        except Exception,e:
            print(e)
    def SetName(self,n):
        self.name=n

            
    def RequestServer(self):

        try:
            self.s.send(b"request")
            print("sending Request")
        except Exception,e:
            print ("error "+e)

    def ExitReqServer(self):

        try:
            self.s.send(b"exit")
            print("sending exit")
        except Exception,e:
            print ("error "+e)
            
        
    def sendY(self,Y):
        self.s.send(b"sendedY")
        Y=str(Y)
        
        l=str(len(Y))
        if int(l)< 10:
            Y=Y+"0000000000"
            l=str(len(Y))
       # print "Y is "+Y
        self.s.send(b""+l)
        self.s.send(b""+Y)
        
    def sendX(self,X):
        self.s.send(b"sendedX")
        X=str(X)
        
        l=str(len(X))
        if int(l)< 10:
            X=X+"0000000000"
            l=str(len(X))
        #print "X is "+X
        self.s.send(b""+l)
        self.s.send(b""+X)


        
    def reicevH(self):
        #print "reciev called"
        self.s.send(b"reicevH")
 
    def sendH(self,H):
        self.s.send(b"sendedH")
        H=str(H)
        
        l=str(len(H))
        if int(l) < 10:
            H=H+"0000000000"
            l=str(len(H))
        #print "H is "+H
        self.s.send(b""+l)
        self.s.send(b""+H)

    def sendS(self,S):
        self.s.send(b"sendedS")
        S=str(S)
        
        l=str(len(S))
        if int(l) < 10:
            S=S+"0000000000"
            l=str(len(S))
        #print "S is "+S
        self.s.send(b""+l)
        self.s.send(b""+S)


        
            
    def getUsers(self):
        self.s.send(b"getplayers")
        
    def getInput(self,l):
        x=self.s.recv(l)
        #print ("getinput is"+x)
        return x
    def getTotalUsers(self):
        self.s.send(b"getcount")
        x=self.s.recv(1)
        print (x)
        return x
    
    def can_start(self):
        self.s.send(b"started")
        return


cl=Client()
cl.giveip(cl.getip())

#cl.connectServer(client.getip())
#client.RequestServer()
#client.getTotalUsers()

#print client.servers
#for k, v in client.servers.iteritems():
#    print k,v

