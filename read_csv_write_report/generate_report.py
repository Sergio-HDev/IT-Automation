#!/usr/bin/env python3

import csv


def read_employees(csv_file_location):
    with open(csv_file_location) as file:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        dict_reader_obj = csv.DictReader(file, dialect = 'empDialect')

        employee_list = []
        for data in dict_reader_obj:
            employee_list.append(data)

        return employee_list

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data

def write_report(dictionay, report_file):
    with open(report_file, "w+") as file:
        for k in sorted(dictionary):
            file.write(str(k) + ':' + str(dictionay[k]) + '\n')
        file.close()


employee_list = read_employees("employees.csv")

dictionary = process_data(employee_list)

write_report(dictionary, 'report.txt')
