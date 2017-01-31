from state import state
import numpy as np
from random import random

class mChain:
	def __init__(self):
		self.stateList = []
		self.F = 0
		self.FT = 0
		self.Tau = 0
		self.absorbStates = []
		self.stateIdCount = 0

	def addState(self, name=""):
		self.stateIdCount += 1
		self.stateList.append(state(self.stateIdCount, name))

	def addLink(self, fromState, toState, probability = 0.0):
		self.stateList[fromState - 1].addLink(toState - 1, probability)

	def genF(self):
		self.F = np.zeros((self.stateIdCount, self.stateIdCount))
		for i in range(len(self.stateList)):
			for j in range(len(self.stateList[i].neighbors)):
				self.F[i,self.stateList[i].neighbors[j][0]] = self.stateList[i].neighbors[j][1]
		self.checkF()
		self.FT = np.transpose(self.F)

		#lazy check
	def checkF(self):
		for i in range(len(self.F)):
			if np.sum(self.F[i]) != 1:
				print("Warning: Row " + str(i+1) + " does not have a row-wise sum of 1. \n")
	
	def isErgodic(self):
		if(np.argwhere(self.F == 1)):
			return False
		else:
			return True

	def printF(self):
		print(self.F)
		
	def solveErgodic(self):
		if(not self.isErgodic):
			print("Error: M.C. is absorbing. \n")
			return
		[w,v] = np.linalg.eig(self.FT)
		ind = np.argwhere(w == 1)[0][0]
		return v[:,ind] / sum(v[:,ind])

	def solveAbsorbing(self):
		self.getAbsorbStates()
		self.genTau()
		f = self.get_fs()
		I = np.identity(len(self.Tau))
		tauPrime = I - self.Tau
		tauPrime = np.linalg.inv(tauPrime)
		sln = []
		for i in range(len(f[1,:])):
			sln.append(np.matmul(tauPrime,f[:,i]))
		return sln
		
	def get_fs(self):
		f = []
		temp = 0
		temp = self.F[:,self.absorbStates]
		temp = np.delete(temp, self.absorbStates, axis=0)
		f = temp
		return f

	def genTau(self):
		row = []
		column = []
		for i in range(len(self.F)):
			for j in range(len(self.F)):
				if(len(np.argwhere(self.absorbStates==i))==0 and len(np.argwhere(self.absorbStates==j))==0):
					row.append(self.F[i,j])
			if(len(row)>0):
				column.append(row)
				row = []
		self.Tau = np.array(column)

	##works, but not optimal
	#def nextState(self, P):
	#	x = random()
	#	sort = np.sort(P)
	#	summ = 0
	#	#print(sort)
	#	for i in range(len(sort)):
	#		summ += sort[i]
	#		#print(x, summ)
	#		if(x < summ):
	#			y = np.argwhere(sort[i]== P)
	#			nextState = y[int(round(random()*(len(y)-1),0))][0]
	#			return nextState;

	def getCD(self, P):
		CD = np.zeros(len(P))
		summ = 0
		for i in range(len(CD)):
			summ += P[i]
			CD[i] = summ
		return CD

	def nextState(self, P):
		x = random()
		CD_P = self.getCD(P)
		summ = 0
		for i in range(len(CD_P)):
			if(x < CD_P[i]):
				return i

	def doExperiment(self,P,iterations):
		stateCount = np.zeros(len(P))
		currentState = self.nextState(P)
		stateCount[currentState] +=1

		for i in range(iterations):
			currentState = self.nextState(self.F[currentState,:])
			stateCount[currentState] += 1
		return (stateCount / iterations)

	def simulateErgodic(self, P = 0, iterations = 0, ensembleSize = 1):
		ensemble =[]
		for i in range(ensembleSize):
			ensemble.append(self.doExperiment(P,iterations))

		temp = np.array(ensemble)
		ensemble = []
		for i in range(len(P)):
			ensemble.append(sum(temp[:][:,i]))
		ensemble = np.array(ensemble)
		
		return (ensemble / ensembleSize)

	def multiplyF(self, iterations = 0, P = 0):
		temp = self.FT
		temp = np.linalg.matrix_power(temp, iterations)
		temp = np.matmul(temp, P)
		temp = temp / sum(temp)
		return temp

	def getAbsorbStates(self):
		absorbStates = []
		for i in range(len(self.F)):
			for j in range(len(self.F)):
				if(self.F[i][j] == 1 and i == j):
					absorbStates.append(i)
					break
		self.absorbStates = np.array(absorbStates)

	#could be better, but time.
	def doAbsorbExperiment(self, enterState, iterations):
		counter = 0
		currentState = enterState - 1
		for i in range(iterations):
			currentState = self.nextState(self.F[currentState,:])
			counter += 1
			if(len(np.argwhere(currentState==self.absorbStates))>0):
				break
		return (currentState)

	def simulateAbsorbing(self, enterState, iterations = 0, ensembleSize = 1):
		self.getAbsorbStates()
		stateCount = np.zeros(len(self.F))
		#f is the absorb state to compute probability of entering
		for i in range(ensembleSize):
			stateCount[self.doAbsorbExperiment(enterState, iterations)]+=1
		stateCount = stateCount / ensembleSize
		temp = []
		for i in range(len(stateCount)):
			if(stateCount[i] != 0):
				temp.append(round(stateCount[i],6))
		temp = np.array(temp)
		return temp

	def maxNeighbors(self):
		temp = []
		for i in range(self.stateIdCount):
			temp.append(len(self.stateList[i].neighbors))
		atemp = max(temp)
		del temp
		return atemp
	