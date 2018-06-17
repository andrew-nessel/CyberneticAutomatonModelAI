from CyberneticAutomatonModel import *
import time


inputAlph = ["0+", "1+", "2+", "0-", "1-", "2-"] # 0 this will be food # 1 this will be a bell # 2 will be a light

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


inputs1P = []
inputs2P = []
inputs3P = []

inputs1M = []
inputs2M = []
inputs3M = []

inputs1P.append(InputSymbol("0+", 1))
inputs2P.append(InputSymbol("1+", 0.7))
inputs3P.append(InputSymbol("2+", 0.5))

inputs1M.append(InputSymbol("0-", 1))
inputs2M.append(InputSymbol("1-", 0.7))
inputs3M.append(InputSymbol("2-", 0.5))


print("conditioning light on bell")
for x in range(0,100):
	cy.inputStimulus(inputs2P)
	cy.inputStimulus(inputs3P)
	cy.inputStimulus(inputs2M)
	cy.inputStimulus(inputs3M)
	time.sleep(.5)

print()
time.sleep(1)

print("conditioning bell on food")
for x in range(0,100):
	cy.inputStimulus(inputs1P)
	cy.inputStimulus(inputs2P)
	cy.inputStimulus(inputs1M)
	cy.inputStimulus(inputs2M)
	time.sleep(.5)

print()
time.sleep(1)

print("checking the conditioning on light")
for x in range(0,100):
	cy.inputStimulus(inputs3P)
	cy.inputStimulus(inputs3M)
	time.sleep(.5)

print()
time.sleep(1)

print("attempting extinction of bell")
for x in range(0,100):
	cy.inputStimulus(inputs2P)
	cy.inputStimulus(inputs2M)
	time.sleep(.5)

print()
time.sleep(1)

print("checking the conditioning on light")
for x in range(0,100):
	cy.inputStimulus(inputs3P)
	cy.inputStimulus(inputs3M)
	time.sleep(.5)