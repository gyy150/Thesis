import csv
from random import randrange

with open("../Data_Set/Training.txt", "w") as training_text_file:
    with open("../Data_Set/Testing.txt", "w") as testing_text_file:
        with open('../Data_Set/loader_work_orders_sanitised.csv', newline='') as csvfile:
                data_reader = csv.reader(csvfile)
                for row in data_reader:
                    print(row[4])
                    dice = randrange(4)
                    if dice > 3:
                        print(row[4], file=testing_text_file)
                    else:
                        print(row[4], file=training_text_file)

