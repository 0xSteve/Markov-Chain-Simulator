from mChain import mChain
import numpy as np

#ergodic MC
A = mChain()

A.addState("State One")
A.addState("State Two")
A.addState("State Three")

A.addLink(1, 1, 0.5)
A.addLink(1, 2, 0.5)
A.addLink(2, 1,(1/3))
A.addLink(2, 3,(2/3))
A.addLink(3, 2, (1/5))
A.addLink(3, 3, (4/5))
P = np.array([1/2, 0, 1/2])

A.genF()
#A.printF()
solution = A.solveErgodic()
print("PI* is: " + str(solution) + " (analytic)\n")
solution = A.multiplyF(65, P)
print("PI* is: " + str(solution) + " (F Transpose at inf)\n")
solution = A.simulateErgodic(P, 1000, 1000)
print("PI* is: " + str(solution) + " (simulation)\n")

#absorbing MC
B = mChain()

B.addState("State One")
B.addState("State Two")
B.addState("State Three")
B.addState("State Four")
B.addState("State Five")

B.addLink(1,1,1)
B.addLink(2,1,0.1)
B.addLink(2,3,0.9)
B.addLink(3,2,0.1)
B.addLink(3,4,0.4)
B.addLink(3,1,0.5)
B.addLink(4,4,0.3)
B.addLink(4,3,0.4)
B.addLink(4,5,0.3)
B.addLink(5,5,1)
f = np.array([0.1,0.5,0])
B.genF()
B.printF()

solution = B.simulateAbsorbing(2, 10000, 24000)
print("Absorbing PI* from State 2 is: " + str(solution) + " (simulation)\n")
solution = B.solveAbsorbing()
print("Absorbing PI* is: " + str(solution) + " (analytic)\n")