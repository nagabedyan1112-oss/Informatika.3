salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0  # у нас нет подушки безопасности
current_spend = spend
for month in range(1, months + 1): # в первый месяц рост цен не применяется
    if month > 1:
        current_spend *= (1 + increase)
    deficit = current_spend - salary
    if deficit > 0:
        money_capital += deficit
money_capital = int(money_capital)
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
