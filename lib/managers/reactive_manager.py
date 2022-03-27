from ..building_manager	import BuildingManager
class ReactiveManager(BuildingManager):
	def __init__(self, name, site):
		super().__init__(name, site)
	def specialisedMaintenance(self):
		return []