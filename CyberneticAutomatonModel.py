
import datetime
import random

class Node():
	#This is a wrapper for a state of the automaton
	
	#need accepting?
	#anything else?

	def __init__(self, nid=-1, reward=False, punishment=False, trans=None):
		self.nid = nid
		if trans is None:
			trans = []
		self.isReward = reward             #whether is a reward state
		self.isPunishment = punishment     #whether is a punishment state  
		self.transitions = trans           #list of transitions from this state

	def includesTrans(self, inputC): #WARN not sure if this is fine just checking the input symbol's character
		for transition in self.transitions:
			if transition.inputSymbol.inputCharacter == inputC:
				return True
		return False

	def getTrans(self, inputSym): #TODO Change this (its checking for equal strength) #use char for character check
		for transition in self.transitions:
			if transition.inputSymbol.inputEQ(inputSym.input):
				return transition
		return None

	def getTransOnChar(self, inputC): #this is for input of just the character
		for transition in self.transitions:
			if transition.inputSymbol.inputCharacter == inputC:
				return transition
		return None

	def removeTransition(self, rTransition):
		self.transitions.remove(rTransition.index)

	def addTransition(self, nTransition):
		nTransition.index = len(self.transitions)
		self.transitions.insert(nTransition.index, nTransition)



class Transition():
	#This is a wrapper for transitions between states of the automaton

	def __init__(self, nextN=None, inputSym=None, outputs=None, confidence=0, permanent=False, index=0):
		self.nextNode = nextN                   #the node this transition leads to
		self.inputSymbol = inputSym               #the input symbol that triggers this transition
		self.outputSymbolNodes = outputs             #the output symbol resulting from this transition #TODO This should be a set of symbols #TODO symbols in set should be able to be marked? #TODO these symbols should have probabilities
		if(self.outputSymbolNodes is None):
			self.outputSymbolNodes = []
		self.confidenceLevel = confidence      #the learned confidence for this transition
		self.permanent = permanent
		self.index = index

	def isPermanent(self):
		return self.permanent

	def markPermanent(self):
		self.permanent = True

	def getNextNode(self):
		return self.nextNode

	def getOutputNodesCopy(self):
		nNodes = []
		for outputSymbolNode in self.outputSymbolNodes:
			nNode = outputSymbolNode.getOutputNodeCopy()
			nNodes.append(nNode)
		return nNodes

	def getProbableOutput(self):
		randNum = random.random()
		pick = None
		pickProb = 0
		for outputNode in self.outputSymbolNodes:
			if((outputNode is not None) and (outputNode.outputProb >= randNum)):
				if(outputNode.outputProb >= pickProb):
					pick = outputNode
					pickProb = outputNode.outputProb
		return pick

	def getOutputNodeOnChar(self, outputChar):
		for outputNode in self.outputSymbolNodes:
			if((outputNode is not None) and (outputNode.outputSymbol.output == outputChar)):
				return outputNode
		return None


class InputSymbol():

	def __init__(self, inputC=None, strength=0):
		self.inputCharacter = inputC
		self.strength = strength

	def inputEQ(self, otherInput):
		if(self.inputCharacter == otherInput.inputCharacter) and (self.strength == otherInput.strength):
			return True
		return False

class OutputSymbol():

	def __init__(self, output=None, strength=0):
		self.output = output
		self.strength = strength

	def outputEQ(self, otherOutput):
		if(self.output == otherOutput.output) and (self.strength == otherInput.strength):
			return True
		return False

	def outputEQOnChar(self, otherOutput):
		if(self.output == otherOutput.output):
			return True
		return False


class OutputNode():

	def __init__(self, outputSymbol=None, outputProb=0, outputMark=False, markedAtTime=0):
		self.outputSymbol = outputSymbol
		self.outputProb = outputProb
		self.outputMark = outputMark
		if ((outputMark) and (markedAtTime == 0)):
			markedAtTime = datetime.datetime.now().timestamp()
		self.markedAtTime = markedAtTime

	def getOutputNodeCopy(self):
		nSymbol = OutputSymbol(self.outputSymbol.output, self.outputSymbol.strength)
		nNode = OutputNode(nSymbol, self.outputProb, self.outputMark)

	def markOutput(self):
		self.outputMark = True
		markedAtTime = datetime.datetime.now().timestamp()

	def markOutputAtTime(self, time):
		self.outputMark = True
		if(time == 0):
			markedAtTime = datetime.datetime.now().timestamp()

	def clearMark(self):
		self.outputMark = False
		self.markedAtTime = 0


class Expectation():

	def __init__(self, initialNode=None, initialInputChar=None, expectedNode=None, expectedInputChar=None, expectationStrength=0):
		self.initialNode = initialNode
		self.initialInputChar = initialInputChar
		self.expectedNode = expectedNode
		self.expectedInputChar = expectedInputChar
		self.expectationStrength = expectationStrength

	def expectationEQ(self, otherExpectation):
		if(self.initialNode.nid != otherExpectation.initialNode.nid):
			return False
		if(self.initialInputChar != otherExpectation.initialInputChar):
			return False
		if(self.expectedNode.nid != otherExpectation.expectedNode.nid):
			return False
		if(self.expectedInputChar != otherExpectation.expectedInputChar):
			return False
		return True



class CyberneticAutomatonModel():


	#Add input/output alphabet?
	#Add expectations structure or should this be in Node/Transition?

	def __init__(self, inputAlphabet=None, outputAlphabet=None, nodeSet=None, startNode=None, expectationSet=None):      #TODO Not finished
		self.inputAlphabet = inputAlphabet           #This is the set of all characters in the input alphabet #TODO replace with some data structure holding all inputs
		if(self.inputAlphabet is None):
			self.inputAlphabet = []
		
		self.outputAlphabet = outputAlphabet          #This is the set of all characters in the output alphabet #TODO replace with some data structure holding all outputs
		if(self.outputAlphabet is None):
			self.outputAlphabet = []

		self.nodeSet = nodeSet                 #This is the set of all states in the model #TODO replace with some data structure holding all nodes
		if(self.nodeSet is None):
			self.nodeSet = []

		self.startNode = startNode               #This is our starting state                 #TODO replace with some start node
		self.currentNode = self.startNode   #This keeps track of what state the model is in (starts in the starting state)
		#self.punishmentSet = None           #This is the set of all punishment states   #TODO replace with some data structure holding all punishment nodes
		#self.rewardSet = None                        #This is the set of all reward states       #TODO replace with some data structure holding all reward nodes
		self.expectationSet = expectationSet           #This is the set of all expectations in the model #TODO replace with some data structure holding all expectations
		if(self.expectationSet is None):
			self.expectationSet = []

		self.intervalTime = datetime.datetime.now().timestamp()  #keeps track of time between last input and now
		self.anchor = startNode
		self.inputL = None

		self.markedOutputs = []
		for node in self.nodeSet:
			for tran in node.transitions:
				for outputSym in tran.outputSymbolNodes:
					if(outputSym.outputMark):
						markedOutputs.append(outputSym)
		self.sortMarkedOutputs()

		#1
		self.c = self.startNode
		self.t = None
		self.ql = self.startNode
		self.al = None
		self.o = None
		self.ol = None
		#should I save last transition?

		#the constants

		self.expectationsAlpha = 0.05             #α
		self.confidenceBeta = 0.05                #β
		self.conditioningSpeedGamma = 0.4         #γ
		self.supervisedLearningSpeedZeta = 0.001  #ζ
		self.conditioningProbabilityNu = 0.5      #ν
		self.recentLearningKappa = 0.9            #κ
		self.initialProbabilityEta = 1.0          #η
		self.timingDifferencialTau = .10          #τ .1s


	def inputStimulus(self, inputSymbols): #TODO Not finished
		
		#2
		timeNow = datetime.datetime.now().timestamp()
		#print(timeNow - self.intervalTime)
		timeDiff = timeNow - self.intervalTime
		while timeDiff > self.timingDifferencialTau:
			if self.c.includesTrans(None):
				tran = self.c.getTransOnChar(None)
				if tran.isPermanent():
					tran.markPermanent()
				self.ql = self.c
				self.c = tran.getNextNode()
			self.anchor = self.c
			self.a1 = None
			self.ol = None
			#NOT FINISHED -> Unmark all symbols b and distributions P∆q,a
			timeDiff -= self.timingDifferencialTau
			#go to step 2? is the while fine?

		self.intervalTime = timeNow

		#3 inputSymbols is a list of inputs and inputL is last input

		#4
		domInput = self.getMaxStrengthInput(inputSymbols)

		#5
		self.createNewTransition(inputSymbols) #5

		#6
		self.ql = self.c
		self.al = domInput.inputCharacter
		self.ol = self.o 
		
		#9
		self.t = self.c.getTransOnChar(domInput.inputCharacter) #TODO should this be only the dominant input or random based on probability on strengths
		self.c = self.t.getNextNode() #TODO I moved this after the conditioning
		
		#7
		self.o = self.t.getProbableOutput()
		if (self.o is not None):
			self.o.outputSymbol.strength = (domInput.strength*self.t.confidenceLevel) / (1+self.t.confidenceLevel) #TODO Actually output this somehow
			print(self.o.outputSymbol.output)
		else:
			self.o = OutputNode(OutputSymbol(None, 0), 0, False, 0)
			print("None")

		#8
		self.o.markOutput()


		#10
		self.updateExpectations(inputSymbols) #10 update with parameters and return values

		#11
		if(self.c.isReward):
			self.applyReward() #update with parameters and return values
		elif(self.c.isPunishment):
			self.applyPunishment() #update with parameters and return values
		else:
			self.applyConditioning(inputSymbols) #update with parameters and return values

		#self.c = self.t.getNextNode() #TODO this is normally in 9 and happens before conditioning

		self.inputL = inputSymbols
		return


	def createNewTransition(self, inputSymbols):		
		if self.c.includesTrans(None):
			tran = self.c.getTransOnChar(None)
			if not tran.isPermanent():
				self.c.removeTransition(tran)
		for inputS in inputSymbols:
			if not (self.c.includesTrans(inputS.inputCharacter)):
				newQ = Node(self.getNextNodeId(), False, False, None)
				self.addNodeToQSet(newQ)
				transToNew = Transition(newQ, inputS, None, 0, True, 0)
				transToAnchor = Transition(self.anchor, InputSymbol(None, 0), None, 0, False, 0)
				self.c.addTransition(transToNew)
				self.c.addTransition(transToAnchor)
				transPrime = self.getOtherTransitionOnInputCharacter(inputS)
				if(transPrime is None):
					transToNew.outputSymbolNodes.append(OutputSymbolNode(OutputSymbol(None, 0), self.initialProbabilityEta, False))
					#transToNew.outputSymbolNodes.append(OutputSymbolNode(OutputSymbol("BetaSymbol", (1-self.initialProbabilityEta)/(abs(DELTA)-1)), self.initialProbabilityEta, False)) #TODO Fix this, its saying to add an input symbol of Beta but Beta is a number? and using some DELTA value that is undefined
					transToNew.confidenceLevel = 0.1
				else:
					transToNew.outputSymbolNodes = transPrime.getOutputNodesCopy()
					transToNew.confidenceLevel = transPrime.confidenceLevel


	def updateExpectations(self, inputSymbols):
		
		domInput = self.getMaxStrengthInput(inputSymbols)

		if(self.includesExpectation(self.ql, self.al, self.c, domInput.inputCharacter)):
			ex1 = self.getExpectation(self.ql, self.al, self.c, domInput.inputCharacter)
			tr1 = self.ql.getTransOnChar(self.al)
			changeInEx1 = self.expectationsAlpha*(1 - ex1.expectationStrength)
			ex1.expectationStrength += changeInEx1
			tr1.confidenceLevel = tr1.confidenceLevel*(1 - self.confidenceBeta*(abs(changeInEx1)))


			ex2 = self.getExpectation(self.c, domInput.inputCharacter, self.ql, self.al)
			tr2 = self.c.getTransOnChar(domInput.inputCharacter)
			changeInEx2 = self.expectationsAlpha*(1 - ex2.expectationStrength)
			ex2.expectationStrength += changeInEx2
			tr2.confidenceLevel = tr2.confidenceLevel*(1 - self.confidenceBeta*(abs(changeInEx2)))
		else:
			self.expectationSet.append(Expectation(self.ql, self.al, self.c, domInput.inputCharacter, self.expectationsAlpha))
			self.expectationSet.append(Expectation(self.c, domInput.inputCharacter, self.ql, self.al, self.expectationsAlpha))

		for ai in self.inputAlphabet:
			if ((self.includesExpectation(self.ql, self.al, self.c, ai)) and not (self.charInInputs(inputSymbols, ai))):
				ex = self.getExpectation(self.ql, self.al, self.c, ai)
				tr = self.ql.getTransOnChar(self.al)
				changeInEx = self.expectationsAlpha*(1 - ex.expectationStrength)
				ex.expectationStrength += changeInEx
				tr.confidenceLevel = tr.confidenceLevel*(1 - self.confidenceBeta*(abs(changeInEx)))

		for q in self.nodeSet:
			if(q.nid != self.ql.nid):
				for ai in self.inputAlphabet:
					if(ai != self.al):
						if(self.includesExpectation(self.c, domInput.inputCharacter, q, ai)):  #TODO check this the expectation its checking included is different from the expectation that its modifying, this seems to be in the book this way, make sure this is right
							ex = self.getExpectation(q, ai, self.c, domInput.inputCharacter)
							tr = self.c.getTransOnChar(ai)
							changeInEx = 0-self.expectationsAlpha*(ex.expectationStrength)
							ex.expectationStrength += changeInEx
							tr.confidenceLevel = tr.confidenceLevel*(1 - self.confidenceBeta*(abs(changeInEx)))


		for ai in self.inputAlphabet:
				for bi in self.inputAlphabet:
					if(ai != bi):
						if (self.charInInputs(inputSymbols, ai) and self.charInInputs(inputSymbols, bi)):
							if(self.includesExpectation(self.c, ai, q, bi)):
								ex = self.getExpectation(self.c, ai, self.c, bi)
								tr = self.c.getTransOnChar(ai)
								changeInEx = self.expectationsAlpha*(1 - ex.expectationStrength)
								ex.expectationStrength += changeInEx
								tr.confidenceLevel = tr.confidenceLevel*(1 - self.confidenceBeta*(abs(changeInEx)))

						elif (self.charInInputs(inputSymbols, ai) or self.charInInputs(inputSymbols, bi)):
							if(self.includesExpectation(self.c, ai, q, bi)):
								ex = self.getExpectation(self.c, ai, self.c, bi)
								tr = self.c.getTransOnChar(ai)
								changeInEx = 0-self.expectationsAlpha*(ex.expectationStrength)
								ex.expectationStrength += changeInEx
								tr.confidenceLevel = tr.confidenceLevel*(1 - self.confidenceBeta*(abs(changeInEx)))
	

		#TODO remove this crap
		#self.expectationsAlpha = 0.05             #α
		#self.confidenceBeta = 0.05                #β
		#self.conditioningSpeedGamma = 0.4         #γ
		#self.supervisedLearningSpeedZeta = 0.001  #ζ
		#self.conditioningProbabilityNu = 0.5      #ν
		#self.recentLearningKappa = 0.9            #κ
		#self.initialProbabilityEta = 1.0          #η
		#self.timingDifferencialTau = .10          #τ .1s

	def applyReward(self, inputSymbols): #TODO Not finished
		domInput = self.getMaxStrengthInput(inputSymbols)
		t = 1
		transitionsMarked = self.getTransitionsMarkedSorted()
		for transition in transitionsMarked:
			for outputNode in transition.outputSymbolNodes:
				if(outputNode.outputMark):
					outputNode.outputProb = (outputNode.outputProb+self.supervisedLearningSpeedZeta*t*domInput.strength*(1/transition.confidenceLevel))/(1+self.supervisedLearningSpeedZeta*t*domInput.strength*(1/transition.confidenceLevel))
					outputNode.clearMark()
				else:
					outputNode.outputProb = (outputNode.outputProb)/(1+self.supervisedLearningSpeedZeta*t*domInput.strength*(1/transition.confidenceLevel))
				transition.confidenceLevel += self.supervisedLearningSpeedZeta*t*domInput.strength
				for trans in (self.getOtherTransitionListOnInputCharacter(outputNode.outputSymbol.output)):
					for outputNodeT in trans.outputSymbolNodes:
						if(outputNodeT.outputMark):
							outputNodeT.outputProb = (outputNodeT.outputProb+self.supervisedLearningSpeedZeta*t*domInput.strength*(1/trans.confidenceLevel))/(1+self.supervisedLearningSpeedZeta*t*domInput.strength*(1/trans.confidenceLevel))
							outputNodeT.clearMark()
						else:
							outputNodeT.outputProb = (outputNodeT.outputProb)/(1+self.supervisedLearningSpeedZeta*t*domInput.strength*(1/trans.confidenceLevel))
					trans.confidenceLevel = self.conditioningProbabilityNu*self.supervisedLearningSpeedZeta*t*domInput.strength

			self.removeTransitionFromMarked()
			t = recentLearningKappa*t
		return

	def applyPunishment(self): #TODO Not finished (copy of reward)
		domInput = self.getMaxStrengthInput(inputSymbols)
		t = 1
		transitionsMarked = self.getTransitionsMarkedSorted()
		for transition in transitionsMarked:
			for outputNode in transition.outputSymbolNodes:
				if(outputNode.outputMark):
					outputNode.outputProb = (outputNode.outputProb+self.supervisedLearningSpeedZeta*t*domInput.strength*(1/transition.confidenceLevel))/(1+self.supervisedLearningSpeedZeta*t*domInput.strength*(1/transition.confidenceLevel))
					outputNode.clearMark()
				else:
					outputNode.outputProb = (outputNode.outputProb)/(1+self.supervisedLearningSpeedZeta*t*domInput.strength*(1/transition.confidenceLevel))
				transition.confidenceLevel += self.supervisedLearningSpeedZeta*t*domInput.strength
				for trans in (self.getOtherTransitionListOnInputCharacter(outputNode.outputSymbol.output)):
					for outputNodeT in trans.outputSymbolNodes:
						if(outputNodeT.outputMark):
							outputNodeT.outputProb = (outputNodeT.outputProb+self.supervisedLearningSpeedZeta*t*domInput.strength*(1/trans.confidenceLevel))/(1+self.supervisedLearningSpeedZeta*t*domInput.strength*(1/trans.confidenceLevel))
							outputNodeT.clearMark()
						else:
							outputNodeT.outputProb = (outputNodeT.outputProb)/(1+self.supervisedLearningSpeedZeta*t*domInput.strength*(1/trans.confidenceLevel))
					trans.confidenceLevel = self.conditioningProbabilityNu*self.supervisedLearningSpeedZeta*t*domInput.strength

			self.removeTransitionFromMarked()
			t = recentLearningKappa*t
		return

	def applyConditioning(self, inputSymbols): #TODO Check if my change made sense
		domInput = self.getMaxStrengthInput(inputSymbols)
		
		if (self.ol is not None) and (self.ol.outputSymbol.outputEQOnChar(self.o.outputSymbol)):
			for ai in self.inputAlphabet:
				if ((self.includesExpectation(self.ql, self.al, self.ql, ai)) and (self.charInInputs(inputSymbols, ai))):
					tr = self.ql.getTransOnChar(ai)
					trOutputNode = tr.getOutputNodeOnChar(self.ol.outputSymbol.output)

					if(trOutputNode is None):
						tr.confidenceLevel += self.conditioningSpeedGamma*domInput.strength
						self.updateConditioning(self.ql, ai, domInput.strength*(1/tr.confidenceLevel), inputSymbols)
					else:
						trOutputNode.outputProb = (trOutputNode.outputProb + self.conditioningSpeedGamma*domInput.strength*(1/(tr.confidenceLevel)))/(1 + (self.conditioningSpeedGamma*domInput.strength*(1/tr.confidenceLevel)))
						for outputNode in tr.outputSymbolNodes:
							if (not (outputNode.outputSymbol.outputEQOnChar(self.ol.outputSymbol))):
								outputNode.outputProb = (outputNode.outputProb)/(1 + (self.conditioningSpeedGamma*domInput.strength*(1/tr.confidenceLevel)))

			for q in self.nodeSet:
				for ai in self.inputAlphabet:
					if(q.includesTrans(ai) and q.getTransOnChar(ai).getNextNode().nid == self.ql.nid):
						tr = q.getTransOnChar(ai)
						trOutputNode = tr.getOutputNodeOnChar(self.ol.outputSymbol.output)

						if(trOutputNode is None):
							tr.confidenceLevel += self.conditioningSpeedGamma*domInput.strength
							self.updateConditioning(q, ai, domInput.strength*(1/tr.confidenceLevel), inputSymbols)
						else:
							trOutputNode.outputProb = (trOutputNode.outputProb + self.conditioningSpeedGamma*domInput.strength*(1/(tr.confidenceLevel)))/(1 + (self.conditioningSpeedGamma*domInput.strength*(1/tr.confidenceLevel)))
							for outputNode in tr.outputSymbolNodes:
								if (not (outputNode.outputSymbol.outputEQOnChar(self.ol.outputSymbol))):
									outputNode.outputProb = (outputNode.outputProb)/(1 + (self.conditioningSpeedGamma*domInput.strength*(1/tr.confidenceLevel)))

	def updateConditioning(self, nodePrime, outputCharacterPrime, outputStrength, inputSymbols): 
		if(outputStrength > 0.001): #floating point numbers will be the death of me
			for ai in self.inputAlphabet:
				if (self.includesExpectation(nodePrime, outputCharacterPrime, nodePrime, ai)):
					tr = nodePrime.getTransOnChar(ai)
					trOutputNode = tr.getOutputNodeOnChar(self.ol.outputSymbol.output)
					if(trOutputNode is not None):
						trOutputNode.outputProb = (trOutputNode.outputProb + self.conditioningSpeedGamma*outputStrength*(1/(tr.confidenceLevel)))/(1 + (self.conditioningSpeedGamma*outputStrength*(1/tr.confidenceLevel)))
						for outputNode in tr.outputSymbolNodes:
							if (not (outputNode.outputSymbol.outputEQOnChar(self.ol.outputSymbol))):
								outputNode.outputProb = (outputNode.outputProb)/(1 + (self.conditioningSpeedGamma*outputStrength*(1/tr.confidenceLevel)))

			for q in self.nodeSet:
				for ai in self.inputAlphabet:
					if(q.includesTrans(ai) and q.getTransOnChar(ai).getNextNode().nid == nodePrime.nid):
						if (self.includesExpectation(nodePrime, outputCharacterPrime, q, ai)):
							tr = q.getTransOnChar(ai)
							trOutputNode = tr.getOutputNodeOnChar(self.ol.outputSymbol.output)
							#TODO changed this next line from transition of qPrime->aPrime to q->a
							trOutputNode.outputProb = (trOutputNode.outputProb + self.conditioningSpeedGamma*outputStrength*(1/(tr.confidenceLevel)))/(1 + (self.conditioningSpeedGamma*outputStrength*(1/tr.confidenceLevel)))
							for outputNode in tr.outputSymbolNodes:
								if (not (outputNode.outputSymbol.outputEQOnChar(self.ol.outputSymbol))):
									outputNode.outputProb = (outputNode.outputProb)/(1 + (self.conditioningSpeedGamma*outputStrength*(1/tr.confidenceLevel)))


			for ai in self.inputAlphabet:
				if (self.includesExpectation(nodePrime, outputCharacterPrime, nodePrime, ai)):
					if (self.charInInputs(inputSymbols, ai)):
						#TODO changed this next line from transition of qPrime->aPrime to qPrime->a
						tr = nodePrime.getTransOnChar(ai)
						trOutputNode = tr.getOutputNodeOnChar(self.ol.outputSymbol.output)
						if(trOutputNode is None):
							tr.confidenceLevel += self.conditioningSpeedGamma*outputStrength
							print(tr.confidenceLevel)
							print(outputStrength*(1/tr.confidenceLevel))
							self.updateConditioning(nodePrime, ai, outputStrength*(1/tr.confidenceLevel), inputSymbols)

			for q in self.nodeSet:
				for ai in self.inputAlphabet:
					if(q.includesTrans(ai) and q.getTransOnChar(ai).getNextNode().nid == self.ql.nid): #TODO check if this should be checking for transition to NODEPRIME
						if (self.includesExpectation(nodePrime, outputCharacterPrime, q, ai)):
							tr = q.getTransOnChar(ai)
							trOutputNode = tr.getOutputNodeOnChar(self.ol.outputSymbol.output)
							if(trOutputNode is None):
								tr.confidenceLevel += self.conditioningSpeedGamma*outputStrength
								print(tr.confidenceLevel)
								print(outputStrength*(1/tr.confidenceLevel))
								self.updateConditioning(q, ai, outputStrength*(1/tr.confidenceLevel), inputSymbols)

	def getMaxStrengthInput(self, inputSyms):
		mStrength = -1
		mStrengthInput = None
		for inputSym in inputSyms:
			if (inputSym.strength > mStrength):
				mStrength = inputSym.strength
				mStrengthInput = inputSym
		return mStrengthInput

	def addNodeToQSet(self, newNode):
		for node in self.nodeSet:
			if(node.nid == newNode):
				return
		self.nodeSet.append(newNode)
		return

	def getNextNodeId(self):
		return len(self.nodeSet)

	def includesExpectation(self, q1, a1, q2, a2):
		for expect in self.expectationSet:
			if (expect.expectationEQ(Expectation(q1, a1, q2, a2))):
				return True
		return False

	def getExpectation(self, q1, a1, q2, a2):
		for expect in self.expectationSet:
			if (expect.expectationEQ(Expectation(q1, a1, q2, a2))):
				return expect
		return None

	def charInInputs(self, inputSymbols, inputChar):
		for inputSymbol in inputSymbols:
			if (inputSymbol.inputCharacter == inputChar):
				return True
		return False

	def getOtherTransitionOnInputCharacter(self, inputSymbol):
		for q in self.nodeSet:
			if (q.includesTrans(inputSymbol.inputCharacter)):
				return q.getTransOnChar(inputSymbol.inputCharacter)
		return None

	def getOtherTransitionListOnInputCharacter(self, inputSymbol):
		transitionList = []
		for q in self.nodeSet:
			if (q.includesTrans(inputSymbol.inputCharacter)):
				transitionList.append(getTransOnChar(inputSymbol.inputCharacter))
		return transitionList


	def sortMarkedOutputs(self):
		return

	def getLastOutput(self):
		return self.o


#print (datetime.datetime.now().timestamp())