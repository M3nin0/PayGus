class Day(object):
	def __init__(self, day_number, value):
		"""Construtor
		:param: day_number (int): Número do dia no mês
		:param: value (int): Valor gasto no dia
		"""
		self.__day_number = day_number
		self.__value = value

	@property
	def day_number(self):
		return self.__day_number

	@property
	def value(self):
		return self.__value

class Month(object):
	def __init__(self, month_number):
		"""Construtor
		:param: month_number (int): Número do mês criado
		"""
		self.__month_number = month_number
		self.__days = []

	def add_day(self, day):
		self.__days.append(day)

	@property
	def month_number(self):
		return self.__month_number

	@property
	def days(self):
		return self.__days
