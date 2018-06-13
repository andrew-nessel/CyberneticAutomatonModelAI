
import datetime

def Node():
	#This is a wrapper for a state of the automaton
	
	#need accepting?
	#anything else?

	def __init__(self, reward=False, punishment=False, trans=None):
		if trans is None:
			trans = list(Transition)
		self.isReward = reward             #whether is a reward state
		self.isPunishment = punishment     #whether is a punishment state  
		self.transitions = trans           #list of transitions from this state

	def includesTrans(self, input):
		for transition in self.trans:
			if transition.inputSymbol == input:
				return True
		return False

	def getTrans(self, input): #TODO is this an okay transition function? feels like it needs probability...
		for transition in self.trans:
			if transition.inputSymbol == input:
				return transition
		return None



def Transition():
	#This is a wrapper for transitions between states of the automaton

	def __init__(self, next=None, input=None, output=None, confidence=0, permanent=False):
		self.nextNode = next                   #the node this transition leads to
		self.inputSymbol = input               #the input symbol that triggers this transition
		self.outputSymbol = output             #the output symbol resulting from this transition
		self.confidenceLevel = confidence      #the learned confidence for this transition
		self.permanent = permanent

	def isPermanent(self):
		return self.permanent

	def markPermanent(self):
		self.permanent = True

	def nextNode(self):
		return self.nextNode

def InputSymbol():

	def __init__(self, input=None, strength=0):
		self.input = input
		self.strength = strength


def CyberneticAutomatonModel():

	expectationsAlpha = 0          #α
	confidenceBeta = 0             #β
	conditioningSpeedGamma = 0     #γ
	learningSpeedZeta = 0          #ζ
	conditioningProbabilityNu = 0  #ν
	recentLearningKappa = 0        #κ
	initialProbabilityEta = 0      #η
	timingDifferencialTau = 0      #τ


	#Add input/output alphabet?
	#Add expectations structure or should this be in Node/Transition?

	def __init__(self):      #TODO Not finished
		self.nodeSet = None                 #This is the set of all states in the model #TODO replace with some data structure holding all nodes
		self.startNode = None               #This is our starting state                 #TODO replace with some start node
		self.currentNode = self.startNode   #This keeps track of what state the model is in (starts in the starting state)
		self.punishmentSet = None           #This is the set of all punishment states   #TODO replace with some data structure holding all punishment nodes
		self.rewardSet = None                        #This is the set of all reward states       #TODO replace with some data structure holding all reward nodes
		
		self.intervalTime = datetime.datetime.now().timestamp()  #keeps track of time between last input and now
		self.anchor = startNode
		self.inputL = None

		self.c = self.startNode
		self.ql = self.startNode
		self.al = None
		self.o = None
		self.ol = None


	def inputStimulus(self, inputSymbols): #TODO Not finished
		
		timeNow = datetime.datetime.now().timestamp()
		timeDiff = timeNow - self.intervalTime
		while timeDiff > timingDifferencialTau:
			if self.c.includesTrans(None):
				tran = self.c.getTrans(None)
				if tran.isPermanent():
					tran.markPermanent()
				self.ql = self.c
				self.c = tran.nextNode()
			self.anchor = self.c
			self.a1 = None
			self.ol = None
			#NOT FINISHED -> Unmark all symbols b and distributions P∆q,a
			timeDiff -= timingDifferencialTau

		self.intervalTime = timeNow

		#4

		createNewTransition() #5 update with parameters and return values

		#6,7,8,9

		updateExpectations() #10 update with parameters and return values

		if(self.c.isReward):
			applyReward() #update with parameters and return values
		else if(self.c.isPunishment):
			applyPunishment() #update with parameters and return values
		else:
			applyConditioning() #update with parameters and return values

		#12 is a loop? a loop in the function, or should be called a number of times? if called careful of scope of variables

		self.inputL = inputSymbols
		return None  #Finished 1, 2~, 3, NOT FINISHED 4+

	def createNewTransition(): #TODO Not finished
		return None

	def updateExpectations(): #TODO Not finished
		return None

	def applyReward(): #TODO Not finished
		return None

	def applyPunishment(): #TODO Not finished
		return None

	def applyConditioning(): #TODO Not finished
		return None

	def updateConditioning(): #TODO Not finished
		return None


print (datetime.datetime.now().timestamp())