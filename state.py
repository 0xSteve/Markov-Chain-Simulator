class state:
	def __init__(self, id, name = ""):
		self.id = id
		self.name = name
		self.neighbors = []
		self.counter = 0

	def addLink(self, toStateId, probability):
		self.neighbors.append([toStateId, probability])

	def __del__(self):
		del self.id
		del self.name
		del self.neighbors
		del self.counter