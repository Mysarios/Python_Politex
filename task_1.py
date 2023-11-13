import json
# TODO решите задачу
def task() -> float:
    result = 0
    with open ('input.json','r') as file:
        data = json.load(file)
    for i in range(len(data)):
        result += data[i]["score"] * data[i]["weight"]
    return round(result,3)


print(task())