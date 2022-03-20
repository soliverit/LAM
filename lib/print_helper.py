class PrintHelper():
	##
	# Translate 2D array into a formatted table
	##
	@staticmethod
	def formatArray(array):
		maxCells	= 0
		for row in array:
			if len(row) > maxCells:
				maxCells = len(row)
		rowWidth	= 0
		cellWidths	= [0 for x in range(maxCells)]
		for rowID in range(len(array)):
			row 	= array[rowID]
			for cellID in range(len(row)):
				if isinstance(row[cellID], str) and len(str(row[cellID]))> cellWidths[cellID]:
					cellWidths[cellID] = len(row[cellID])
		formatted	= []
		for row in array:
			rowString	= ""
			cells		= []
			for cellID in range(len(row)):
				cell = str(row[cellID])
				while len(cell) < cellWidths[cellID]:
					cell += " "
				cells.append(cell)
			formatted.append(" | ".join(cells))
		print("\n".join(formatted))
			
			
				
		
				
		