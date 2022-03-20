class History():
	def __init__(self):
		self.readings	= []
	def addReading(self, reading):
		self.readings.append(reading)
	def length(self):
		return len(self.readings)
	