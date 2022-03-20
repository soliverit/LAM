class Zone():
	def __init__(self, name, area):
		self.name			= name
		self.area			= area
		self.sensors		= []
		self.sensorsHash	= {}
		self.luminaires		= []
	def addSensor(self, sensor):
		self.sensors.append(sensor)
		if sensor.__class__.__name__ not in self.sensorsHash:
			self.sensorsHash[sensor.__class__.__name__]	= []
		self.sensorsHash[sensor.__class__.__name__].append(sensor)
	def addLuminaire(self, luminaire):
		self.luminaires.append(luminaire)
	def co2Sensors(self):
		return self.sensorsHash["CO2Sensor"]
	def thermometers(self):
		return self.sensorsHash["Thermometer"]
	def takeReadings(self):
		for luminaire in self.luminaires:
			luminaire.takeReading()
		for sensor in self.sensors:
			sensor.takeReading()
	def broken(self):
		broken	= []
		for luminaire in self.luminaires:
			if luminaire.isBroken():
				broken.append(luminaire)
		for sensor in self.sensors:
			if sensor.isBroken():
				broken.append(sensor)
		return broken
	def needMaintenance(self, threshold):
		needMaintenance	= []
		for luminaire in self.luminaire:
			if luminaire.worthMaintaining(threshold):
				needMaintenance.append(lumianire)
		return needMaintenance