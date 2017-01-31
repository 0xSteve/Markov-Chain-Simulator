from mChain import mChain
import numpy as np


#TRAFFIC LIGHTS!
A = mChain()

#states
A.addState("1")
A.addState("2")
A.addState("3")
A.addState("4")
#links
A.addLink(1,1,0.5)
A.addLink(1,2,0.5)
A.addLink(2,1,0.1)
A.addLink(2,2,0.1)
A.addLink(2,4,0.2)
A.addLink(2,3,0.6)
A.addLink(3,3,0.5)
A.addLink(3,4,0.5)
A.addLink(4,2,0.8)
A.addLink(4,4,0.2)
P = np.array([1,0,0,0])

#get F
A.genF()
#A.printF()
solution = A.solveErgodic()
print("PI* is: " + str(solution) + " (analytic)\n")
solution = A.multiplyF(65, P)
print("PI* is: " + str(solution) + " (F Transpose at inf)\n")
solution = A.simulateErgodic(P, 1000, 1000)
print("Ergodic PI* of C is: " + str(solution) + " (simulation)\n")
