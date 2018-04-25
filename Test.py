import csv
import re
from random import randrange

test_matchcase1 = re.compile(r'((\w*[\w\s])\/([\w\s]\w*))')
test_matchcase2 = re.compile(r'(\s[a-z]{2,4}[\d|\s]\d{1,4})[\s|.]')
test_matchcase3 = re.compile(r'[a-z]{3}\s\d+')
test_matchcase4 = re.compile(r'[a-z]{3}(?!\s\d+)')

test_matchcase5 = re.compile(r'\s[0-9]{2}/[0-9]{2}/[0-9]{2,4}')
test_matchcase6 = re.compile(r'\w+\/\w+')
test_matchcase7 = re.compile(r'(^|\s)(r and r)\d')
test_matchcase8 = re.compile('trd_number_(?=l_number_|\s)')
test_matchcase9 = re.compile(r'(she(\s_|_)number_)')
a = "bv she _number_ ins air / con pect _number_ damage equipment_id reportr o/ haul and r1 10/20 construction soil  trd_number_ l_number_ test she_number_ and r2 construction soil test she_number_ edd 0081& edd 59 sign skids worn engine constantly derating/stalling through derating /stalling RegExr v3 edd3455  created by gskinner.com, an rd0222."

if __name__ == '__main__':
    #a = re.sub('&', ' and ', a)
    #print(a)
    result = test_matchcase1.findall(a)
    print(result)
    for t in result:
        t0 = t[1].strip()
        t1 = t[2].strip()
        if len(t0) + len(t1) > 7:
            string_to_replace = t0 + ' ' + t1
        else:
            string_to_replace = t0 + '_' + t1
        print(string_to_replace)
        result = re.sub(test_matchcase1.pattern , string_to_replace , a)
        print(result)












#
# with open('../Data_Set/loader_work_orders_sanitised.csv', newline='') as csvfile:
#     data_reader = csv.reader(csvfile)
#     for row in data_reader:
#         short_text = row[4]
#
#         short_text = re.sub('&', ' and ', short_text)
#
#         found_string = regex.findall(short_text)
#         if len(found_string) > 0 :
#             short_text = re.sub('\w\/\w', found_string[0].replace('/', ''), short_text)
#
#         short_text = re.sub('\d+', ' ', short_text)
#         short_text = re.sub('\W+', ' ', short_text)
#
#         #if len(short_text) > 2 and short_text[-1] == '.':
#         #   short_text = short_text[:-1]
#
#         print(short_text.split())
#
#
# with open("../Data_Set/Training.txt", "w") as training_text_file:
#     with open("../Data_Set/Testing.txt", "w") as testing_text_file:
#         with open('../Data_Set/loader_work_orders_sanitised.csv', newline='') as csvfile:
#                 data_reader = csv.reader(csvfile)
#                 for row in data_reader:
#                     short_text = row[4]
#                     print(short_text.split())
#                     dice = randrange(4)
#                     if dice > 3:
#                         print(row[4], file=testing_text_file)
#                     else:
#                         print(row[4], file=training_text_file)

