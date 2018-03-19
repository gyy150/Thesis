import csv
import re
from random import randrange

regex = re.compile(r'\w\/\w')

with open('../Data_Set/loader_work_orders_sanitised.csv', newline='') as csvfile:
    data_reader = csv.reader(csvfile)
    for row in data_reader:
        short_text = row[4]


        found_string = regex.findall(short_text)
        if len(found_string) > 0 :
            short_text = re.sub('\w\/\w', found_string[0].replace('/', ''), short_text)

        short_text = re.sub('\d+', ' ', short_text)
        short_text = re.sub('\W+', ' ', short_text)

        #if len(short_text) > 2 and short_text[-1] == '.':
        #   short_text = short_text[:-1]

        print(short_text.split())


with open("../Data_Set/Training.txt", "w") as training_text_file:
    with open("../Data_Set/Testing.txt", "w") as testing_text_file:
        with open('../Data_Set/loader_work_orders_sanitised.csv', newline='') as csvfile:
                data_reader = csv.reader(csvfile)
                for row in data_reader:
                    short_text = row[4]
                    print(short_text.split())
                    dice = randrange(4)
                    if dice > 3:
                        print(row[4], file=testing_text_file)
                    else:
                        print(row[4], file=training_text_file)

