money_capital: float = 0
salary = 50000
spend: float = 45000
increase: float = 1.03
count_month = 10

#Комментарий про первый месяц все такой же,но я внес ег ов цикл

for i in range(0, count_month):
    money_capital += salary - spend
    spend *= increase

print("Ur capital must be {:.2f} money  to live for 10 months".format(money_capital * -1))