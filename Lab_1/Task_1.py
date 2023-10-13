List = [0, 1, 2, 3, 4, None, 5, 8, 7]
print(List)

Sum = 0
Empty_index = 0
i = 0

for number in List:
    if number == None:
        Empty_index = i
    else:
        Sum += number
    i += 1

List[Empty_index] = Sum / (len(List) - 1)

print(List)
