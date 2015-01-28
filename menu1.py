import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from panda3d.core import *
from client import *
import socket
import time
from direct.showbase.ShowBase import ShowBase
class Menu:
    def __init__(self):        
        self.count=0
        self.x={}
        self.y={}
        self.z={}
        self.Gstart=0
        self.slist=False
        self.nlist=False
        self.connected=False
        self.music = loader.loadSfx("sounds/music/menu.wav")
        self.engine = loader.loadSfx("sounds/sfx/engine5.wav")

        self.engine.setLoop(True)
        self.engine.setVolume(.7)
        self.music.setLoop(True)
        self.music.setVolume(.7)
        self.music.play()
        
        self.name=""
        self.font = loader.loadFont("cmr12.egg")
        self.myImage=OnscreenImage(image = 'bg.jpg', pos = (0, 0, 0),scale=(2,2,1))
        
        self.myImage.setTransparency(TransparencyAttrib.MAlpha)
        self.welcome=OnscreenText(text = "Welcome to 3d multiplayer Racing Game",fg=Vec4(1,1,1,1),shadow=Vec4(0,0,0,1),scale=0.10,pos=(0,.8,0))
        self.bk_text = " "
        self.textObject = OnscreenText(text = self.bk_text, pos = (0.95,-0.95),
                                  scale = 0.07,fg=(1,0.5,0.5,0),align=TextNode.ACenter,mayChange=1,font=self.font,shadow=Vec4(0,0,0,1),bg=(1,1,1,.2))
        

        self.b = DirectEntry(scale=.05,command=self.setText,initialText="Enter your name",
                             numLines = 1,focus=0,focusInCommand=self.clearText,
                             entryFont=self.font,width=20,
                             pos=(-0.5,0,0),borderWidth=(0.5,0.5),color=(1,1,1,0.5),autoCapitalize=1)
        self.b.setTransparency(TransparencyAttrib.MDual )        
    def setText(self,textEntered):
        
        self.name=textEntered
        cl.SetName(self.name)
        
        self.textObject.setText("Welcome  "+textEntered)
        self.client()

    def createDirectlist(self):
        
        numItemsVisible = 4
        itemHeight = 0.11
        myScrolledList = DirectScrolledList(
            decButton_pos= (0.35, 0, 0.53),
            decButton_text = "Dec",
            decButton_text_scale = 0.04,
            decButton_borderWidth = (0.005, 0.005),
            incButton_pos= (0.35, 0, -0.02),
            incButton_text = "Inc",
            incButton_text_scale = 0.04,
            incButton_borderWidth = (0.005, 0.005),
            frameSize = (0.0, 0.7, -0.05, 0.59),
            frameColor = (1,0,0,0.5),
            pos = (-1, 0, 0),  
            numItemsVisible = numItemsVisible,
            forceHeight = itemHeight,
            itemFrame_frameSize = (-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos = (0.35, 0, 0.4),
            )
        return myScrolledList

    
    def clearText(self):
        self.b['color']=Vec4(1,1,1,1)
        self.b.enterText('')

    def client(self):
        self.b.destroy()
        self.textObject['fg']=Vec4(1,1,1,1)

        self.refresh = DirectButton(text = ("", "", "", "disabled"),scale=.05,
                         command=self.refresh,pos = (0.95,-0.95,0),image="refresh.png",image_scale=2)
        self.refresh.setTransparency( TransparencyAttrib.MAlpha )


        

    def refresh(self):
        if self.slist:
            self.slist.destroy()

        if self.nlist:
            self.nlist.destroy()

        if self.connected:
            self.getMembers()
        else:
            for k, v in cl.servers.iteritems():
                self.addserver(k,v)
        
    def addserver(self,k,v):
        print "inside addserver()"
        self.slist=self.createDirectlist()
    
        self.x[self.count]=k
        self.y[self.count]=v
        self.z[self.count]= DirectButton(text =v, scale=.05, command=self.connectServer,extraArgs=str(self.count))
        self.slist.addItem(self.z[self.count])
        self.count=self.count+1
        
    def clearServers(self):
        for i in range(0,self.count):
            self.z[i].destroy()

        self.slist.destroy()
        self.count=0
    def connectServer(self,count):
        #print count
        #print self.x[int(count)]
        self.slist.destroy()
        self.connected=True
        

        self.clearServers()

        cl.connectServer(str(self.x[int(count)]))
        
        self.getMembers()

    def getMembers(self):
        
        self.nlist=self.createDirectlist()
        cl.RequestServer()
        x=int(cl.getTotalUsers())
        cl.RequestServer()
        cl.getUsers()
        for i in range(0,x):
             l=cl.getInput(1)
             k=cl.getInput(int(l))
             l = DirectLabel(text = str(k), text_scale=0.05)
             self.nlist.addItem(l) 
        if x >1 :
            self.start = DirectButton(text = ("", "", "", "disabled"),scale=.05,
                         command=self.destroy,pos = (0.2,-0.95,0),image="start.jpg",image_scale=2)
            self.start.setTransparency( TransparencyAttrib.MAlpha )
        cl.ExitReqServer()
        #self.c.RequestServer()
        #self.c.getTotalUsers()
        #self.c.getTotalUsers(s)
    def sendY(self,Y):
        cl.sendY(Y)

    def sendH(self,H):
        cl.sendH(H)       
        
    def destroy(self):
         self.Gstart=1;
         self.nlist.destroy()
         self.myImage.destroy()
         self.welcome.destroy()
         self.b.destroy()
         self.textObject.destroy()
         self.start.destroy()
         self.start.destroy()
         self.refresh.destroy()
         
         self.self=None
         
         return
