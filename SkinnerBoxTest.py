from CyberneticAutomatonModel import *
import time

#NOT FINISHED JUST COPY

inputAlph = ["F", "1N", "1E", "1S", "1W", "2N", "2E", "2S", "2W", None] 

outputAlph = ["M", "L", "R", "B"]


nodeS = []
node0 = Node(0, False, False, None)
node1 = Node(1, False, False, None)
node2 = Node(2, False, False, None)
node3 = Node(3, False, False, None)
node4 = Node(4, False, False, None)
node5 = Node(5, False, False, None)
node6 = Node(6, False, False, None)
node7 = Node(7, False, False, None)
nodeR = Node(8, True, False, None)
nodeQs = Node(9, False, False, None)


#make outputs??

trans1N = Transition(node1, InputSymbol("1N", 0), None, 10, True, 0)
trans1E = Transition(node2, InputSymbol("1E", 0), None, 10, True, 0)
trans1S = Transition(node3, InputSymbol("1S", 0), None, 10, True, 0)
trans1W = Transition(node4, InputSymbol("1W", 0), None, 10, True, 0)
trans2N = Transition(node5, InputSymbol("2N", 0), None, 10, True, 0)
trans2E = Transition(node6, InputSymbol("2E", 0), None, 10, True, 0)
trans2S = Transition(node7, InputSymbol("2S", 0), None, 10, True, 0)
trans2W = Transition(nodeQs, InputSymbol("2W", 0), None, 10, True, 0)
transR = Transition(nodeR, InputSymbol("F", 0), None, 10, True, 0)

node0.transitions.append(trans1N)
node0.transitions.append(trans1E)
node0.transitions.append(trans1S)
node0.transitions.append(trans1W)
node0.transitions.append(trans2N)
node0.transitions.append(trans2E)
node0.transitions.append(trans2S)
node0.transitions.append(trans2W)
node0.transitions.append(transR)

nodeS.append(node0)
nodeS.append(node1)
nodeS.append(node2)
nodeS.append(node3)
nodeS.append(node4)
nodeS.append(node5)
nodeS.append(node6)
nodeS.append(node7)
nodeS.append(nodeR)
nodeS.append(nodeQs)

startN = node0 #Make some node from nodeS



cy = CyberneticAutomatonModel(inputAlph, outputAlph, nodeS, startN, None)

#make actual test

inputs1N = []
inputs1E = []
inputs1S = []
inputs1W = []
inputs2N = []
inputs2E = []
inputs2S = []
inputs2W = []
inputsF = []
inputsNone = []

inputs1N.append(InputSymbol("1N", 1))
inputs1E.append(InputSymbol("1E", 1))
inputs1S.append(InputSymbol("1S", 1))
inputs1W.append(InputSymbol("1W", 1))
inputs2N.append(InputSymbol("2N", 1))
inputs2E.append(InputSymbol("2E", 1))
inputs2S.append(InputSymbol("2S", 1))
inputs2W.append(InputSymbol("2W", 1))
inputsF.append(InputSymbol("F", 1))
inputsNone.append(InputSymbol(None, 1))

currentPosition = "1N"

cy.inputStimulus(inputs1N)

print("starting skinner box test")
for x in range(0,100):
	output = cy.getLastOutput()

	if(currentPosition == "1N"):
		if(output is None):
			#do something about this
			cy.inputStimulus(inputs1N)
		elif(output.outSymbol.output == "L"):
			cy.inputStimulus(inputs1E)
		elif(output.outSymbol.output == "R"):
			cy.inputStimulus(inputs1W)
		else:
			cy.inputStimulus(inputs1N)

	elif(currentPosition == "1E"):
		if(output is None):
			#do something about this
			cy.inputStimulus(inputs1E)
		elif(output.outSymbol.output == "L"):
			cy.inputStimulus(inputs1S)
		elif(output.outSymbol.output == "R"):
			cy.inputStimulus(inputs1N)
		else:
			cy.inputStimulus(inputs1E)

	elif(currentPosition == "1S"):
		if(output is None):
			#do something about this
			cy.inputStimulus(inputs1S)
		elif(output.outSymbol.output == "L"):
			cy.inputStimulus(inputs1W)
		elif(output.outSymbol.output == "R"):
			cy.inputStimulus(inputs1E)
		else:
			cy.inputStimulus(inputs1S)

	elif(currentPosition == "1W"):
		if(output is None):
			#do something about this
			cy.inputStimulus(inputs1W)
		elif(output.outSymbol.output == "M"):
			cy.inputStimulus(inputs2W)
		elif(output.outSymbol.output == "L"):
			cy.inputStimulus(inputs1N)
		elif(output.outSymbol.output == "R"):
			cy.inputStimulus(inputs1S)
		else:
			cy.inputStimulus(inputs1W)

	elif(currentPosition == "2N"):
		if(output is None):
			#do something about this
			cy.inputStimulus(inputs2N)
		elif(output.outSymbol.output == "L"):
			cy.inputStimulus(inputs2E)			
		elif(output.outSymbol.output == "R"):
			cy.inputStimulus(inputs2W)
		else:
			cy.inputStimulus(inputs2N)

	elif(currentPosition == "2E"):
		if(output is None):
			#do something about this
			cy.inputStimulus(inputs2E)
		elif(output.outSymbol.output == "M"):
			cy.inputStimulus(inputs1E)
		elif(output.outSymbol.output == "L"):
			cy.inputStimulus(inputs2S)
		elif(output.outSymbol.output == "R"):
			cy.inputStimulus(inputs2N)
		else:
			cy.inputStimulus(inputs2E)

	elif(currentPosition == "2S"):
		if(output is None):
			#do something about this
			cy.inputStimulus(inputs2S)
		elif(output.outSymbol.output == "L"):
			cy.inputStimulus(inputs2W)
		elif(output.outSymbol.output == "R"):
			cy.inputStimulus(inputs2E)
		else:
			cy.inputStimulus(inputs2S)

	elif(currentPosition == "2W"):
		if(output is None):
			#do something about this
			cy.inputStimulus(inputs2W)
		elif(output.outSymbol.output == "B"):
			cy.inputStimulus(inputsR)
		elif(output.outSymbol.output == "L"):
			cy.inputStimulus(inputs2N)
		elif(output.outSymbol.output == "R"):
			cy.inputStimulus(inputs2S)
		else:
			cy.inputStimulus(inputs2W)			
		
	#time.sleep(.5)

#print()
#time.sleep(1)
