# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    delimiter_csv = ','
    with open(INPUT_FILENAME,'r', newline='') as file:
        csvData = csv.DictReader(file, delimiter = delimiter_csv)

        dataForJson = []
        for row in csvData:
            dataForJson.append(row)
            with open(OUTPUT_FILENAME, 'w') as file:
                json.dump(dataForJson, file, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
