from ..asset	import Asset
class Sensor(Asset):
	def __init__(self, name, minReading, maxReading, maintenanceCycle, faultProbability):
		super().__init__(name, minReading, maxReading, maintenanceCycle, faultProbability)