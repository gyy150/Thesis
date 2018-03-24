import csv
import re

class Sentences_Parser(object):
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.Match_Case = re.compile(r'\w\/\w')

    def process_short_text(self , short_text):
        found_string = self.Match_Case.findall(short_text)

        if len(found_string) > 7:
            short_text = re.sub('\w\/\w', found_string[0].replace('/', ' '), short_text)

        if len(found_string) > 0 and len(found_string) < 7:
            short_text = re.sub('\w\/\w', found_string[0].replace('/', '_'), short_text)

        short_text = re.sub('&', ' and ', short_text)
        short_text = re.sub('@', ' at ', short_text)
        short_text = re.sub(r"'+", '', short_text)
        short_text = re.sub('\d+', ' ', short_text)
        #short_text = re.sub('\W+', ' ', short_text)
        short_text = re.sub('[^_\w]+', ' ', short_text)

        return short_text

    def __iter__(self):

        with open(self.dir_name + 'loader_work_orders_sanitised.csv', newline='') as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                short_text = row[4]
                short_text = self.process_short_text(short_text)

                yield short_text.split()


def Print_Out_Resuls(sentences):
    with open("../Data_Cleaning/Cleaned_Data.txt", "w") as cleaned_data_file:
        i = 1
        for sentence in sentences:
            string_to_print = str(i) + '\t' + " ".join(sentence)
            print( string_to_print , file=cleaned_data_file)
            i = i +1




if __name__ == "__main__":
    sentences = Sentences_Parser('../Data_Set/')
    Print_Out_Resuls(sentences)