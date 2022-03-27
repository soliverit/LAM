## Includes
# Native

#
from .assets.luminaire		import Luminaire
from .assets.co2_sensor		import	CO2Sensor
from .assets.thermometer	import Thermometer
from .building_manager		import BuildingManager
from .zone					import Zone
class Site():
	def __init__(self, name,area):
		self.name		= name		# string name of the site (address basically, doesn't matter)
		self.zones		= []		# [Zone()] where the Zones go!
		self.area		= 0			# Volu... nope. Area m²
		self.manager	= False		# Something that inherits from BuildingManager
	
	### Add stuff ###
	def addZone(self, zone):
		self.zones.append(zone)
		self.area	+= zone.area
		
	### Getters ###
	def luminaires(self):
		luminaires	= []
		for zone in self.zones:
			luminaires += zone.luminaires
		return luminaires
	def co2Sensors(self):
		sensors	 = []
		for zone in self.zones:
			if "CO2Sensor" in zone.sensorsHash:
				sensors += zone.sensorsHash["CO2Sensor"]
		return sensors
	def thermometers(self):
		sensors	 = []
		for zone in self.zones:
			if "Thermometer" in zone.sensorsHash:
				sensors += zone.sensorsHash["Thermometer"]
		return sensors
		
	### Readings stuff ###
	def takeReadings(self):
		for zone in self.zones:
			zone.takeReadings()
			
	### Misc / ah'll get to categorising it eventually ###
	def sensorsReadingBounds(self, type):
		results	= {"lowest": 99999, "highest": -999999}
		
		for zone in self.zones:
			if type not in zone.sensorsHash:
				break
			for sensor in zone.sensorsHash[type]:
				if sensor.lowestReading < results["lowest"]:
					results["lowest"] 	= sensor.lowestReading
				elif sensor.highestReading > results["highest"]:
					results["highest"]	= sensor.highestReading
		return results
	
	### Static / class stuff ###
	##
	# Parse one entry from the ./data/test.jsonj. Basically,
	# a SBEM model but instead of energy information, there's
	# a bunch of assets. Luminaires, CO2/Temp sensors, and
	# cabinets. 
	#
	# Note: cabinet's aren't part of this yet. Might
	# add the later if it's necessary
	##
	@staticmethod
	def fromJSON(data):
		print("WARNING!!!! Site::fromJSON only adding 5 sensors to zone. for test performance")
		site		= Site(data["name"], data["area"])
		for hvac in data["hvacs"]:
			zonesJSON	= hvac["zones"]
			for zoneID in range(len(zonesJSON)):
				zoneJSON	= zonesJSON[zoneID]
				zone		= Zone(site.name + " - " + str(zoneID), zoneJSON["area"])
				zoneName	= site.name + "::" + zone.name + "::luminaire-"
				site.addZone(zone)
				for sensorID in range(len(zoneJSON["sensors"])):
					if sensorID > 4:
						break
					sensorJSON	= zoneJSON["sensors"][sensorID]
					sensorClass	= CO2Sensor if sensorJSON["type"] == "co2" else Thermometer	# Dirty dirty dirty! (don't need more)
					sensor		= sensorClass(zoneName	+ "::" + str(sensorID), sensorJSON["lower_limit"], sensorJSON["upper_limit"])
					zone.addSensor(sensor)
				for luminaireID in range(zoneJSON["luminaires"]):
					zone.addLuminaire(
						Luminaire(
							zoneName + str(luminaireID),
							zoneJSON["wattage"] / zone.area
						)
					)
		return site
			