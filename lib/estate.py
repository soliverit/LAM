## Includes
# Native
from json 			import loads
# Project
from .site			import Site
from .print_helper	import PrintHelper as P
class Estate():
	def __init__(self, name, manager):
		self.name		= name
		self.manager	= manager
		self.sites	= []
	def addSite(self, site):
		self.sites.append(site)
	def filterDuplicateSites(self):
		sites		= {}
		filtered	= []
		for site in self.sites:
			sites[site.name]	= site
		for key in list(sites):
			filtered.append(sites[key])
		self.sites	= filtered
	
	def takeReadings(self):
		for site in self.sites:
			site.takeReadings()
	def summary(self):
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
	@staticmethod
	def ParseJSON(path):
		estate	= Estate("Estate from: " + path)
		with open(path) as dataFile:
			data	= loads(dataFile.read())
		for site in data["sites"]:
			estate.addSite(Site.fromJSON(site))
		return estate
	