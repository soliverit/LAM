## Includes
# Native
from os							import system
# Project
from lib.estate					import Estate
from lib.site					import Site
from lib.managers				import ReactiveManager
from lib.managers				import PrevantativeManager

from lib.assets.co2_sensor		import CO2Sensor
from lib.assets.thermometer		import Thermometer
from lib.assets.luminaire		import Luminaire

estate = Estate.ParseJSON("C:\\repos\\maintenance_strategy_optimisation\\data\\test.json", ReactiveManager("Reactive Dave"))
estate.filterDuplicateSites()
estate.sites	= estate.sites[0: 20]
for i in range(1000):
	estate.takeReadings()
	if (i + 100) % 200 == 0:
		system("cls")
		print("Iteration: " + str(i))
		estate.summary()	

