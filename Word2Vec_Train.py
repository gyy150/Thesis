import gensim
import csv
import re

class MySentences(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.regex = re.compile(r'\w\/\w')

    def __iter__(self):

        with open('../Data_Set/loader_work_orders_sanitised.csv', newline='') as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                short_text = row[4]
                found_string = self.regex.findall(short_text)

                if len(found_string) > 0 :
                    short_text = re.sub('\w\/\w', found_string[0].replace('/', 'UNDERSCORE'), short_text)

                short_text = re.sub('\d+', ' ', short_text)
                short_text = re.sub('\W+', ' ', short_text)
                yield short_text.split()

#        with open('../Data_Set/loader_work_orders_sanitised.csv', newline='') as csvfile:
#                data_reader = csv.reader(csvfile)
#                for row in data_reader:
#                    short_text = row[4]
#                    short_text = re.sub('\W+', ' ', short_text)

 #                   if len(short_text) > 2 and short_text[-1] == '.':
 #                       short_text = short_text[:-1]



sentences = MySentences('../Data_Set')  # a memory-friendly iterator

##for s in sentences:
##    print(s)

model = gensim.models.Word2Vec(sentences , min_count= 2 ,  size=200 ,  workers=4)
model.save('../Data_Set/mymodel_1')

