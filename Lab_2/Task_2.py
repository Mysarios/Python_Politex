money_capital: float = 0
salary = 50000
spend: float = 45000
increase: float = 1.03

# First month
money_capital += salary - spend

for i in range(1, 10):
    money_capital += salary - spend
    spend *= increase

print("Ur capital must be {:.2f} money  to live for 10 months".format(money_capital * -1))
print("Ur last spend = %d " % spend)