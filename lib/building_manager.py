from .work_package	import WorkPackage
class BuildingManager():
	def __init__(self, name, site):
		self.name		= name
		self.site		= site
		self.requests	= []
		self.maintainThreshold	= 0.9
	def evaluateSite(self):
		brokenThings	= self.reactiveMaintenance()
		otherThings		= self.specialisedMaintenance()
		return WorkPackage(site, brokenThings, otherThings)
	def reactiveMaintenance(self):
		broken	= []
		for zone in self.site.zones:
			for asset in zone.broken():
				broken.append(asset)
		return broken
	def specialisedMaintenance(self):
		raise "BuildingManager: specialisedMaintenance method has not been overridden"