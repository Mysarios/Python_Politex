money_capital: float = 2159.78
salary = 50000
spend: float = 45000
increase: float = 1.05
count_month = 0

# First month
money_capital += salary - spend
if money_capital > 0:
    count_month = 1
    while round(money_capital) > 0:
        money_capital += salary - spend
        spend *= increase
        count_month += 1
print("U can live %d  month" % count_month)
print("Ur last spend = %d " % spend)
