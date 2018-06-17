from CyberneticAutomatonModel import *
import time

#NOT FINISHED JUST COPY

inputAlph = ["PP", "PN", "NP", "NN", "B", "F"] 

outputAlph = ["L", "R", None]


nodeS = []
node0 = Node(0, False, False, None)
node1 = Node(1, False, False, None)
node2 = Node(2, False, False, None)
node3 = Node(3, False, False, None)
node4 = Node(4, False, False, None)
nodeR = Node(5, False, False, None)
nodeP = Node(6, False, False, None)


#make outputs??

trans1Outputs = []
trans1Outputs.append(OutputNode(OutputSymbol("01", 0.8), 1, False, 0))

trans1 = Transition(node1, InputSymbol("PP", 0), None, 10, True, 0)
trans2 = Transition(node2, InputSymbol("PN", 0), None, 10, True, 0)
trans3 = Transition(node3, InputSymbol("NP", 0), None, 10, True, 0)
trans4 = Transition(node4, InputSymbol("NN", 0), None, 10, True, 0)
transR = Transition(nodeR, InputSymbol("B", 0), None, 10, True, 0)
transB = Transition(nodeP, InputSymbol("F", 0), None, 10, True, 0)

node0.transitions.append(trans1)
node0.transitions.append(trans2)
node0.transitions.append(trans3)
node0.transitions.append(trans4)
node0.transitions.append(transR)
node0.transitions.append(transB)


nodeS.append(node0)
nodeS.append(node1)
nodeS.append(node2)
nodeS.append(node3)
nodeS.append(node4)
nodeS.append(nodeR)
nodeS.append(nodeP)

startN = node0 #Make some node from nodeS



cy = CyberneticAutomatonModel(inputAlph, outputAlph, nodeS, startN, None)


inputsPP = []
inputsPN = []
inputsNP = []
inputsNN = []
inputsB = []
inputsF = []
inputsPP.append(InputSymbol("PP", 1))
inputsPN.append(InputSymbol("PN", 1))
inputsNP.append(InputSymbol("NP", 1))
inputsNN.append(InputSymbol("NN", 1))
inputsB.append(InputSymbol("B", 1))
inputsF.append(InputSymbol("F", 1))


#make actual test