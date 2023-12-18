import json

# Чтение значений из файлов
with open('tests.json', 'r') as tests_file:
    tests_data = json.load(tests_file)

with open('values.json', 'r') as values_file:
    values_data = json.load(values_file)


# Формирование отчета на основании результатов тестов
def fill_report(tests_data, values_data):
    for test in tests_data:
        if 'id' in test and test['id'] in values_data:
            test['value'] = values_data[test['id']]
        if 'children' in test:
            fill_report(test['children'], values_data)


# Заполнение отчета
fill_report(tests_data, values_data)

# Запись отчета в файл report.json
with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)
