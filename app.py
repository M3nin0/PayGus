from paygus.models.calc import DayCalculator
from paygus.models.time_space import Day, Month

if __name__ == '__main__':

	day_calculator = DayCalculator(lambda day: day.value * 2)
	
	june = Month(7)
	june.add_day(Day(23, 4.50))
	june.add_day(Day(22, 4.50))

	day_calculator.calculate(june)

	print('Actual value: {}'.format(day_calculator.current_total))
