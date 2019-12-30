class evaltree:
   def __init__(self,board,player):
      self.b=board
      self.v=-999.9
      self.c=[]
      #node:[move,value,[child]]
      self.py=player
      self.d=0
      #max:odd min:even

   def testB(self,move):
      if len(move)!=2:
         return False
      tboard=list(self.b)
      pre=move[0]
      post=move[1]
      piece=tboard[pre]
      tboard[post]=piece
      tboard[pre]=0
      return tboard

   def addChild(self,moveList):
      childDep=self.d+1
      length=len(moveList)
      for move in moveList:
         tboard=self.testB(move)
         child=evaltree(tboard,self.py)
         child.d=childDep
         self.c.append(child)
      return True

   def updateVal(self,level):
      if level==0:
         self.v=self.evaluateBoard()
         return True
      depth=self.d
      childVal=[]
      for child in self.c:
         child.updateVal(level-1)
         childVal.append(child.v)
      if depth%2==0:#max
         self.v=max(childVal)
      elif depth%2==1:#min
         self.v=min(childVal)
      return True

   def evaluateBoard(self):
      accum=0
      board=self.b
      for i in range(0,63):
         if board[i]!=0:
            accum=accum+self.pieceValue(i)
      return accum

   def pieceValue(self,pos):
      piece=self.b[pos]
      board=self.b
      if board[pos]==0:
         return 0
      py=self.py
      rval=0
      if (piece/10)*10==py:
         s=1
      elif (piece/10)*10==(30-py):
         s=-1
      else:
         return rval
      
      if piece%10==0: #pawns
         rval=1.0
      elif piece%10==1: #knight
         rval=3.0
      elif piece%10==2: #bishop
         rval=3.0
      elif piece%10==3: #rook
         rval=5.0
      elif piece%10==4: #queen
         rval=9.0
      elif piece%10==5: #king
         rval=90.0
      else:
         return False
      return s*rval

class queue:
   def __init__(self):
      self.store=[]

   def enqueue(self,x):
      self.store=self.store+x

   def dequeue(self):
      if len(self.store)==0:
         return [False,0]
      else:
         rval=self.store[0].c
         self.store=self.store[1:len(self.store)]
         return [True,rval]
 
  
def GetLevelOrder(tree):
   x=queue()
   x.enqueue([tree])
   accum=[]
   v=[]
   while True:
      y=x.dequeue()
      if (y[0]==False):
         break
      else:
         v=y[1]
         for i in v:
            accum=accum+[i.v]
            if len(accum)>256:
               break
            x.enqueue(i.c)
   return accum