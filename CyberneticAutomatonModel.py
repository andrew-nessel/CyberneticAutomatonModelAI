


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



def Transition():
	#This is a wrapper for transitions between states of the automaton

	def __init__(self, next=None, input=None, output=None, confidence=0):
		self.nextNode = next                   #the node this transition leads to
		self.inputSymbol = input               #the input symbol that triggers this transition
		self.outputSymbol = output             #the output symbol resulting from this transition
		self.confidenceLevel = confidence      #the learned confidence for this transition


def CyberneticAutomatonModel():

	#Add input/output alphabet?
	#Add expectations structure or should this be in Node/Transition?

	def __init__(self):      #TODO Not finished
		self.nodeSet = None                 #This is the set of all states in the model #TODO replace with some data structure holding all nodes
		self.startNode = None               #This is our starting state                 #TODO replace with some start node
		self.currentNode = self.startNode   #This keeps track of what state the model is in (starts in the starting state)
		self.punishmentSet = None           #This is the set of all punishment states   #TODO replace with some data structure holding all punishment nodes
		self.rewardSet = None               #This is the set of all reward states       #TODO replace with some data structure holding all reward nodes


	def inputStimulus(): #TODO Not finished
		return None

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



