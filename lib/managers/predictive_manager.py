## Includes
# Native
from random		import random
# Project
from .history	import History
from .reading	import Reading
##
# Abstract'ish class for assets. Luminaires, sensors and whatnot
##
class Asset():
	def __init__(self, name, minReading, maxReading, maintenanceCycle, faultProbability=0):
		self.name				= name
		self.minReading			= minReading
		self.maxReading			= maxReading
		self.faultProbability	= faultProbability
		self.maintenanceCycle	= maintenanceCycle
		self.valueRangeScale	= 1.1
		self.broken				= False
		self.history			= History()
	def takeReading(self):
		time	= len(self.history)	#Time could be anything. I just need an integer
		factor	= random()
		if self.broken or factor < self.faultProbability:
			self.history.append(Reading(0, Reading.CRITICAL_FAILURE)
			self.broken	= True
			return
			
		value	= facotr * self.maxReading * self.valueRangeScale + self.minReading
		if value < self.minReading:
			category	=  Reading.LOW_READING
		elif value > self.maxReading:
			category	= Reading.MAX_READING
		else:
			cateogry	= Reading.OK_READING
		self.history.append(Reading(time, value, category)