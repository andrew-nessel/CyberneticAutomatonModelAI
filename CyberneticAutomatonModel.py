
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

	def getTrans(self, input):
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


	def inputStimulus(inputSymbols): #TODO Not finished
		c = self.startNode
		ql = self.startNode
		al = None
		o = None
		ol = None

		timeNow = datetime.datetime.now().timestamp()
		timeDiff = timeNow - self.intervalTime
		while timeDiff > timingDifferencialTau:
			if c.includesTrans(None):
				tran = c.getTrans(None)
				if tran.isPermanent():
					tran.markPermanent()
				ql = c
				c = tran.nextNode()
			self.anchor = c
			a1 = None
			ol = None
			#NOT FINISHED -> Unmark all symbols b and distributions P∆q,a
			timeDiff -- timingDifferencialTau

		self.intervalTime = timeNow

		#Currently on 4


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