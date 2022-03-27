## Includes
# Native
from os									import system
# Project
from lib.estate							import Estate
from lib.site							import Site
from lib.managers.reactive_manager		import ReactiveManager
from lib.managers.preventative_manager	import PreventativeManager
from lib.critical_path_manager			import CriticalPathManager
from lib.assets.co2_sensor				import CO2Sensor
from lib.assets.thermometer				import Thermometer
from lib.assets.luminaire				import Luminaire

estate = Estate.ParseJSON("C:\\repos\\maintenance_strategy_optimisation\\data\\test.json")
cpm		= CriticalPathManager(estate)
estate.filterDuplicateSites()
estate.sites	= estate.sites[0: 10]
for site in estate.sites:
	site.manager	= ReactiveManager("Reactive Dave", site)
for i in range(10000):
	estate.takeReadings()
	if (i + 100) % 200 == 0:
		system("cls")
		print("Iteration: " + str(i))
		estate.summary()	
	cpm.doTheThing()

