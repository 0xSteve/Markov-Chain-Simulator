from mChain import mChain
import numpy as np
B = mChain()

B.addState("State One")
B.addState("State Two")
B.addState("State Three")
B.addState("State Four")

B.addLink(1,1,1)
B.addLink(2,1,0.1)
B.addLink(2,3,0.9)
B.addLink(3,2,0.1)
B.addLink(3,4,0.4)
B.addLink(3,1,0.5)
B.addLink(4,4,1)
B.genF()
B.printF()

solution = B.solveAbsorbing()
print("Absorbing PI* of B is: " + str(solution) + " (analytic)\n")
solution = B.simulateAbsorbing(2, 10000, 5000)
print("Absorbing PI* of B is: " + str(solution) + " (simulation)\n")

C = mChain()

C.addState("State One")
C.addState("State Two")
C.addState("State Three")
C.addState("State Four")

C.addLink(1,1,1)
C.addLink(2,1,0.1)
C.addLink(2,3,0.9)
C.addLink(3,2,0.5)
C.addLink(3,4,0.3)
C.addLink(3,1,0.2)
C.addLink(4,4,1)
C.genF()
C.printF()

solution = C.solveAbsorbing()
print("Absorbing PI* of C is: " + str(solution) + " (analytic)\n")
solution = C.simulateAbsorbing(2, 10000, 5000)
print("Absorbing PI* of C starting in State 2 is: " + str(solution) + " (simulation)\n")
solution = C.simulateAbsorbing(3, 10000, 5000)
print("Absorbing PI* of C starting in State 3 is: " + str(solution) + " (simulation)\n")