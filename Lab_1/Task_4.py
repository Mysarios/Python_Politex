Visitors = ["Denisov", "Petrov", "Sobolev", "Petrov", "Sobolev", "Sobolev"]

Dictionaty = {
    'All_Visits': 0,
    'Unique':0
}

Visitors_Set = set()
for Human in Visitors:
    Visitors_Set.add(Human)

Dictionaty['All_Visits'] = len(Visitors)
Dictionaty['Unique'] = len(Visitors_Set)

print('All_Visits',Dictionaty['All_Visits'])
print('Unique',Dictionaty['Unique'])