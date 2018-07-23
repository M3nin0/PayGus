# PayGus

Projeto para facilita o controle dos valores gastos com transporte.

## Uso

```Python
from paygus.models.calc import DayCalculator
from paygus.models.time_space import Day, Month

# Cria um objeto do calculador e passa como parâmetro a estratégia de calculo a ser aplicada nos calculos dos valores diários
day_calculator = DayCalculator(lambda day: day.value * 2)

# Criando objeto do mês
june = Month(7)
# Adicionando dias ao mês e seus respectivos valores
june.add_day(Day(23, 4.50))
june.add_day(Day(22, 4.50))

# Realizando calculo do valor gasto no mês
day_calculator.calculate(june)

print('Actual value: {}'.format(day_calculator.current_total))
```
