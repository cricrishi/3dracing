import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from menu1 import *
import thread
import time
class world(DirectObject):
     def __init__(self):
           self.m=Menu()
           #while 1:
           #     if(self.m.Gstart):
            #         car_init()
            #         break;
           taskMgr.add(self.check,"check")
     def check(self,task):
          if(self.m.Gstart):
               cl.can_start()
               opt=cl.getInput(3)
               if opt=="YES":
                  self.car_init()
                  return task.done
          return task.cont
     def car_init(self):
           
           self.m.music.stop()
  
        
	   base.disableMouse()
	   self.m.destroy()

	   self.check_win=-1
	   self.speedy=0
           self.speedx=0
	   self.speed=0
	   self.throttle=0
	   self.maxSpeed = 300
	   self.accel=50
	   self.daccel=20
	   self.handling = 20
	   self.Y1=1052
	   self.X1=-1768
	   self.H1=120.6
	   self.S1=0
	   self.finish=loader.loadModel("finish.egg")
	   self.finish.setPos(-1580,3244,-60)
	   self.finish.reparentTo(render)
	   self.finish.setScale(150,150,100)
	   self.finish.setH(120)
	   base.setBackgroundColor(0,0,0)
	   self.track=loader.loadModel("world/cw")
	   self.car=Actor("quit2.x",{"walk":"quit2.x"})
	   self.mps=OnscreenText(text = "Mps "+str(self.speed),fg=Vec4(1,1,1,1),shadow=Vec4(0,0,0,1),scale=0.10,pos=(-0.8,-0.8,0))
	   self.track.reparentTo(render)
	   self.track.setPos(-1768,1052,-50)
  	   self.car.reparentTo(render)
	   self.car.setPos(29,446,-40)
	   #self.car.setPos(44,437,-40)
	   
	   self.track.setScale(20,20,20)
	   self.car.setScale(5,5,5)
	   self.car.setH(120)
	   self.track.setH(300)
	   base.camera.reparentTo(self.car)
	   base.camera.setY(base.camera,20)
	   base.camera.setZ(base.camera,4)
	   #base.camera.setX(base.camera,8)
	   base.camera.setH(180)

	   self.keyMap ={"arrow_up" : False,
	   "arrow_down":False,
	   "arrow_left":False,
	   "arrow_right":False}
	   
	   self.car.loop("walk")
	   self.other_car()
	   
	   a=1

           thread.start_new_thread(self.timer,(a,))
	   thread.start_new_thread(self.recv_other,(a,))
	   thread.start_new_thread(self.refresh,(a,))

	   
	   taskMgr.doMethodLater(1,self.debugTask,"Debug Task")
	   
	   self.accept("arrow_up", self.setKey, ["arrow_up", True])
	   self.accept("arrow_left", self.setKey, ["arrow_left", True]) 
	   self.accept("arrow_right", self.setKey, ["arrow_right", True])
	   self.accept("arrow_down", self.setKey, ["arrow_down", True])
	   self.accept("arrow_up-up", self.setKey, ["arrow_up", False])
	   self.accept("arrow_down-up", self.setKey, ["arrow_down", False])
	   self.accept("arrow_left-up", self.setKey, ["arrow_left", False])
	   self.accept("arrow_right-up", self.setKey, ["arrow_right", False])

     def timer(self,a):
           time.sleep(2)   
           self.timer=OnscreenText(text = "3",fg=Vec4(1,1,1,1),shadow=Vec4(0,0,0,1),scale=0.40,pos=(0,0,0))
	   time.sleep(2)

           self.timer.setText("2")
           time.sleep(2)
           self.timer.setText("1")
           time.sleep(2)
           self.timer.setText("GO")
           time.sleep(2)
           self.timer.destroy()
           taskMgr.add(self.carMove,"car Move")


     def refresh(self,a):
       try:

        while True :  
          Y1=self.Y1
          X1=self.X1
          H1=self.H1
          

          Y2=self.car1.getY()
          X2=self.car1.getX()
          H2=self.car1.getH()
          
          
          Y=Y2+(Y1-Y2)*.10
          X=X2+(X1-X2)*.10
          H=H2+(H1-H2)*.60

          print ""
          
          self.car1.setY(Y)
          self.car1.setX(X)
          self.car1.setH(H)

       except Exception,e:
            print "error refreshing "+str(e)

     def other_car(self):
           self.car1=Actor("quit3.x",{"walk":"quit3.x"})
	   
	  
	  
  	   self.car1.reparentTo(render)
	   self.car1.setPos(20,380,-40)
	   
	   
	   self.car1.setScale(5,5,5)
	   self.car1.loop("walk")

     def setKey(self,key,value):
          
	     self.keyMap[key]=value

     def turn(self,dir,dt):
          if self.speed != 0:
             turnRate = self.handling * (2 - (self.speed / self.maxSpeed))
          else :
               turnRate = 0
          if(dir == "r"):
               turnRate= -turnRate
          
          
          self.car.setH(self.car, turnRate * dt)
          #S=self.car.getH()
          
          #print "H is"+str(S)   

     def recv_other(self,a):
          try:
           # print "tryingg..."
            flag=1
            while 1:

                 
               dt=.10
               
               X1=self.car1.getX()
	       Y1=self.car1.getY()

	       
               cl.reicevH()          
               x=cl.getInput(2)
               y=cl.getInput(int(x))
               #self.car1.setH(float(y))
               self.H1=float(y)
               #print "H is"+str(y)

               x=cl.getInput(2)
               y=cl.getInput(int(x))
               #self.car1.setY(float(y))
               #print "Y is"+str(y)
               self.Y1=float(y)

               x=cl.getInput(2)
               y=cl.getInput(int(x))
               #self.car1.setX(float(y))
               self.X1=float(y)
               #print "X is"+str(y)
          
               x=cl.getInput(2)
               y=cl.getInput(int(x))
               
               #print "S is"+str(y)

               self.S1=float(y)

               mps=self.S1  
               self.car1.setPlayRate(mps, 'walk')



               self.m.sendH(self.car.getH())

               self.m.sendY(self.car.getY())
               
               cl.sendX(self.car.getX())

               mps=self.speed * 1000/3600

               cl.sendS(mps)

               if flag:
                   self.car1.setH(self.H1)
                   self.car1.setY(self.Y1)
                   self.car1.setX(self.X1)
                   flag=0

               

               
               #print "Y is"+str(y)
          except Exception,e:
               print "error receving..."+str(e)
               
     def carMove(self,task):

           



	   dt=globalClock.getDt()	   
	   if(dt > .20) :
	      return task.cont
	   	  
	   if(self.keyMap["arrow_up"]==True):
	      self.adjustThrottle("up", dt)
	   elif(self.keyMap["arrow_down"]==True): 
	      self.adjustThrottle("down", dt)
	   else:
                self.adjustThrottle(" ", dt)
                
                
                
           if(self.keyMap["arrow_right"]==True):
                self.turn("r",dt)
           elif(self.keyMap["arrow_left"]==True):
                self.turn("l",dt)
	     
	   self.speedCheck(dt)
	   self.move(dt)
	   return task.cont
	   

     def adjustThrottle(self,dir,dt):
          if(dir=="up"):
               self.throttle = 1
               
          elif(dir=="down"):
               self.throttle = -1
               
          else:
               self.throttle = 0
               
                  
               
     def move(self,dt):
          
                       
          #self.car1.setY(self.car1 , -self.S1 * dt)
          mps=self.speed * 1000/3600
          self.mps.setText("Mps "+str(round(mps,1)))
          S=self.car.getY()
          self.car.setPlayRate(mps, 'walk')
          self.car.setY(self.car , -mps * dt)
          S2=self.car.getY()
          S3=self.car.getX()
          if mps > 0:
               self.m.engine.play()
          else:
               self.m.engine.stop()
          #if S!=S2:
           #  self.m.sendY(S2)
           #  cl.sendX(S3)
             #print "Y is"+str(S)
          
     def speedCheck(self,dt):

          if self.speed < 0:
               daccel=self.daccel
          else:
               daccel=-self.daccel
               
          tSetting = (self.maxSpeed * self.throttle)
          if(self.speed < tSetting):
                if((self.speed +(self.accel*dt+daccel*dt)) > tSetting):
			    self.speed = tSetting
	        else:
			
			    self.speed += (self.accel * dt)
	  elif(self.speed > tSetting):
	        if((self.speed-(self.accel * dt+daccel*dt)) < tSetting):
			     self.speed=tSetting
	        else:
			     self.speed -= (self.accel * dt)
						
	  X1=self.car.getX()
	  Y1=self.car.getY()
						
	  X2=self.car1.getX()
	  Y2=self.car1.getY()

	  diffx= X1-X2
	  diffy= Y1-Y2
	  
	  if (diffx < 10 and diffx> - 10):
               if(diffy <10 and diffy> -10):
                    flag=1
               else:
                    flag=0
          else:
               flag=0
               
          
          
          if X1 <-1540 and X1>-1596 and self.check_win==-1 :
               if Y1 < 3304 and Y1> 3197:
                    self.w=OnscreenText(text = "You Win", fg=Vec4(1,1,1,1),shadow=Vec4(0,0,0,1),scale=0.50,pos=(0,0,0))
                    self.check_win=1
                    self.speed=0
          
          if X2 <-1540 and X2>-1596 and self.check_win==-1:
               if Y2 < 3304 and Y2> 3197:
                    self.w=OnscreenText(text = "You Lost", fg=Vec4(1,1,1,1),shadow=Vec4(0,0,0,1),scale=0.50,pos=(0,0,0))
                    self.check_win=0
                    self.speed=0




          
          if self.speed > 0:
               s=1
          else:
               s=-1
          if flag==1: 

               self.speed=-s*10
               if X1 > X2:
                    self.car.setX(X1+5)
               else:
                    self.car.setX(X1-5) 
                         
                    print "collision..."

               
          
     
		
     def debugTask(self,task):
	    
	    return task.again   
     
w=world()
run()
