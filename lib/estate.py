## Includes
# Native
from json 			import loads
# Project
from .site			import Site
from .print_helper	import PrintHelper as P
class Estate():
	##
	# name:		Name of the Estate e.g: Ollie's novelty origami ashtrays limited
	##
	def __init__(self, name):
		self.name					= name
		self.sites					= []
	### Add stuff ###
	##
	# site:		Site()
	##
	def addSite(self, site):
		self.sites.append(site)
	### Filters etc ###
	##
	# WARNING: Ok, a dirty fix for the dev test data.
	##
	def filterDuplicateSites(self):
		sites		= {}
		filtered	= []
		for site in self.sites:
			sites[site.name]	= site
		for key in list(sites):
			filtered.append(sites[key])
		self.sites	= filtered
	### State update stuff ###
	def takeReadings(self):
		for site in self.sites:
			site.takeReadings()
	### Printing etc ###
	##
	# Print a summary of the Site's asset states.
	##
	def summary(self):
		## Headers: The PrintHelper.formatArray method doesn't ask for headers. It's lazy, I'm lazy...
		sites	= [["Name", "Area", "CO2(broken/aging)", "Temp(broken/aging)", "Luminaires(broken/aging)"]]
		for site in self.sites:
			## Luminaires
			luminaires		= site.luminaires()
			broken			= 0
			needsMaintained	= 0
			for luminaire in luminaires:
				if luminaire.broken:
					broken	+= 1
				if luminaire.needsMaintenance:
					needsMaintained	+= 1
			luminaireString	= str(len(luminaires)) + "(" + str(broken) + "/" + str(needsMaintained) + ")"
			## CO2 Sensors
			co2Sensors		= site.co2Sensors()
			broken			= 0 
			needsMaintained	= 0
			for sensor in co2Sensors:
				if sensor.broken:
					broken	+= 1
				if luminaire.needsMaintenance:
					needsMaintained	+= 1	
			co2String	= str(len(co2Sensors)) + "(" + str(broken) + "/" + str(needsMaintained) + ")"
			## Thermometers
			thermometers	= site.thermometers()
			broken = 0
			needsMaintained	= 0
			for sensor in thermometers:
				if sensor.broken:
					broken	+= 1
				if luminaire.needsMaintenance:
					needsMaintained	+= 1	
			thermometerString	= str(len(thermometers)) + "(" + str(broken) + "/" + str(needsMaintained) + ")"
			
			sites.append([site.name[0: 40],str(int(site.area)) + "m²", co2String, thermometerString, luminaireString])
		P.formatArray(sites)
	##
	# Parse JSON (Static)
	#
	#	Parse the training dataset that's kind of just SBEM
	#	models with assets.
	#
	#	returns Estate
	##
	@staticmethod
	def ParseJSON(path):
		estate	= Estate("Estate from: " + path)
		with open(path) as dataFile:
			data	= loads(dataFile.read())
		for site in data["sites"]:
			estate.addSite(Site.fromJSON(site))
		return estate
	