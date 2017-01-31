from mChain import mChain
import numpy as np


#TRAFFIC LIGHTS!
A = mChain()

#states
A.addState("Red")
A.addState("Green")
A.addState("Yellow")
#links
A.addLink(1,2,1)
A.addLink(2,3,1)
A.addLink(3,1,1)

#For safety's sake, let the light start at red
P = np.array([1,0,0])

#get F
A.genF()
A.printF()
solution = A.simulateErgodic(P, 1000, 1000)
print("Ergodic PI* of C is: " + str(solution) + " (simulation)\n")
