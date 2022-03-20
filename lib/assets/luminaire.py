from ..asset import Asset

class Luminaire(Asset):
	DEFAULT_FAULT_PROBABILITY	= 0.001
	DEFAULT_MAINTENANCE_CYCLE	= 400
	def __init__(self, name, wattage):
		super().__init__(name, wattage * 0.9, wattage * 1.1, self.DEFAULT_MAINTENANCE_CYCLE, self.DEFAULT_FAULT_PROBABILITY)
		self.type			= type
		self.wattage		= wattage
		