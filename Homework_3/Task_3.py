import csv
import datetime
import time

with open('new.csv', 'w', encoding='utf-8') as file:
    my_writer = csv.writer(file)
    names_of_columns = ['№', 'Seconds', 'Milliseconds']
    my_writer.writerow(names_of_columns)
    for number in range(1, 301):
        my_writer.writerow([number, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
