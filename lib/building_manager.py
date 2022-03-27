from .work_request	import WorkRequest
class BuildingManager():
	def __init__(self, name, site):
		self.name				= name # String: name alias and or name 
		self.site				= site # Site:   Site managed
		self.maintainThreshold	= 0.9  # Float:  % f total maintenance cycle
	## Get assets ready that are ready for maintenance
	def evaluateSite(self):
		brokenThings	= self.reactiveMaintenance()
		otherThings		= self.preventativeMaintenance()
		return WorkRequest(site, brokenThings, otherThings)
	## Do reactive maintenance: all broken assets. Return []Asset
	def reactiveMaintenance(self):
		broken	= []
		for zone in self.site.zones:
			for asset in zone.broken():
				broken.append(asset)
		return broken
	## Apply instance-specific preventative strategy. Return []Asset
	def preventativeMaintenance(self):
		raise "BuildingManager: specialisedMaintenance hasn't been overridden"