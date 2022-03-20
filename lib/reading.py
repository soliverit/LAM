class Reading():
	OK_READING			= 0
	LOW_READING			= 1
	HIGH_READING		= 2
	CRITICAL_FAILURE	= 3
	STATE_DESCRIPTIONS	= [
		"Reading within expected domain",
		"Reading lower than expected",
		"Reading higher than expected"
		"Reading indicates critical asset failure"
	]
	def __init__(self, time, value, state):
		##
		# Time is really just an index. Could be a timestampe. Here,
		# it's just an int counter
		##
		self.time	= time
		self.value	= value
		self.state	= state