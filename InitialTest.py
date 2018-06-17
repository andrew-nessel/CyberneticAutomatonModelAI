from CyberneticAutomatonModel import *
import time


inputAlph = ["0+", "1+", "0-", "1-"] # 0 this will be food # 1 this will be a bell

outputAlph = ["00", "01", None]  # 00 will be nothing # 01 will be salivation


nodeS = []
node1 = Node(0, False, False, None)
node2 = Node(1, False, False, None)
node3 = Node(2, False, False, None)

trans1Outputs = []
trans1Outputs.append(OutputNode(OutputSymbol("01", 0.8), 1, False, 0))

trans1 = Transition(node2, InputSymbol("0+", 0.8), trans1Outputs, 1000, True, 0)
trans2 = Transition(node3, InputSymbol("0-", 0.8), None, 1000, True, 0)
trans3 = Transition(node1, InputSymbol(None, 0), None, 10, True, 0)

node1.transitions.append(trans1)
node2.transitions.append(trans2)
node3.transitions.append(trans3)

nodeS.append(node1)
nodeS.append(node2)
nodeS.append(node3)

startN = node1 #Make some node from nodeS



cy = CyberneticAutomatonModel(inputAlph, outputAlph, nodeS, startN, None)


inputs1 = []
inputs2 = []
inputs3 = []
inputs4 = []
inputs1.append(InputSymbol("0+", 1))
inputs2.append(InputSymbol("0-", 1))
inputs3.append(InputSymbol("1+", 0.7))
inputs4.append(InputSymbol("1-", 0.7))


print("conditioning bell on food")
for x in range(0,100):
	cy.inputStimulus(inputs1)
	cy.inputStimulus(inputs3)
	cy.inputStimulus(inputs2)
	cy.inputStimulus(inputs4)
	time.sleep(.5)

print()
time.sleep(1)

print("checking if bell is conditioned")
for x in range(0,100):
	cy.inputStimulus(inputs3)
	cy.inputStimulus(inputs4)
	time.sleep(.5)

print()
time.sleep(1)

