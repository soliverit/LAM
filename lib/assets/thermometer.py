from .sensor	import Sensor
class Thermometer(Sensor):
	DEFAULT_FAULT_PROBABILITY	= 0.001
	DEFAULT_MAINTENANCE_CYCLE	= 100
	def __init__(self, name, lowerLimit, upperLimit):
		super().__init__(name, lowerLimit, upperLimit, self.DEFAULT_MAINTENANCE_CYCLE, self.DEFAULT_FAULT_PROBABILITY)
		