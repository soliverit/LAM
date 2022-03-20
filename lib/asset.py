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
	def __init__(self, name, location, minReading, maxReading, maintenanceCycle, faultProbability=0.001):
		self.name				= name					# string
		self.location			= location				# Cooradinate
		self.minReading			= minReading			# float
		self.maxReading			= maxReading			# float
		self.faultProbability	= faultProbability		# float
		self.maintenanceCycle	= maintenanceCycle		# int
		self.lastMaintenance	= 0						# int number of readings since the last maintenance
		self.valueRangeScale	= 1.01					# float
		self.broken				= False					# bool
		self.brokeTime			= 0						# int
		self.history			= History()				# History
		self.lowestReading		= 999999999999999999
		self.highestReading		= -999999999999999999
	def freeze(self):
		if not self.frozen:
			self.frozen	= True
			return True
		return False
	def unfreeze(self):
		if self.frozen:
			self.frozen	= False
			return True
		return False
	def needsMaintenance(self):
		if self.history.length() - self.lastMaintenance > self.maintenanceCycle:
			return True
		return False
	def takeReading(self):
		time		= self.history.length()	#Time could be anything. I just need an integer
		factor		= random()
		if self.broken or factor < self.faultProbability:
			self.history.addReading(Reading(time, 0, Reading.CRITICAL_FAILURE))
			self.broken		= True
			self.brokeTime	+= 1
			return
		value		= factor * self.maxReading * self.valueRangeScale + self.minReading
		if value < self.lowestReading:
			self.lowestReading	= value
		elif value > self.highestReading:
			self.highestReading	= value
		category	= False
		if value < self.minReading:
			category	=  Reading.LOW_READING
		elif value > self.maxReading:
			category	= Reading.HIGH_READING
		else:
			cateogry	= Reading.OK_READING
		self.history.addReading(Reading(time, value, category))