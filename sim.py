import numpy as np
from random import random

F = [[0.5,0.5,0], [1/3,0,2/3], [0,1/5,4/5]]
F = np.array(F)
P = np.array([0.4,0.4,0.2])
stateCount = np.zeros(len(P))
#print(P)


#linear sort
def findState(P):
	x = random()
	count = len(P) -1
	dist = 1
	b=[] 
	while(count >= 0):
		#print(P)
		#print(count)
		a = abs(P[count] - x)
		#print("a: " + str(a))
		#print("dist: " + str(dist)) 
		if(a < dist):
			dist = a
			b = []
			b.append(count)
		elif(a==dist):
			b.append(count)
		count -= 1
		y = random()
	state = b[int(abs(round(y*(len(b) - 1), 0)))]
	return state

def nextState(P):
	x = random()
	sort = np.sort(P)
	summ = 0
	#print(sort)
	for i in range(len(sort)):
		summ += sort[i]
		#print(x, summ)
		if(x < summ):
			y = np.argwhere(sort[i]== P)
			nextState = y[int(round(random()*(len(y)-1),0))][0]
			return nextState;

currentState = nextState(P)
stateCount[currentState] +=1
iterations = 10000

for i in range(iterations):
	currentState = nextState(F[currentState,:])
	stateCount[currentState] += 1

print(stateCount / iterations)




	