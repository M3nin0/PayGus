class DayCalculator(object):
	"""A class to calc the sum of day values
	"""

	def __init__(self, formula):
		"""
		:param: formula: formula used to perform the calculation
		"""
		self.__formula = formula
		self.__current_total = 0

	def calculate(self, month, is_reset = False):
		"""Method to calc the sum of day values
		:param: days list(Day): List with all day objects that need to be calculated 
		:param: is_reset (bool): Tag to indicate if the current total value must be erase
		"""

		if is_reset:
			self.__current_total = 0

		for day in month.days:
			self.__current_total += self.__formula(day) 

	@property
	def formula(self):
		return self.__formula

	@formula.setter
	def formula(self, formula):
		self.__formula = formula

	@property
	def current_total(self):
		return self.__current_total
