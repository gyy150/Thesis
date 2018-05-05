import csv
import re
from collections import defaultdict

class Words_Parser(object):
    def __init__(self, dir_name , file_name ):
        self.file_name = file_name
        self.dir_name  = dir_name

    def __iter__(self):
        with open(self.dir_name + self.file_name , newline='') as words_file:
            for line  in words_file:
                yield line.split()[0]

class Sentences_Parser_3(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __iter__(self):

        with open(self.file_name, "r", newline='') as data_file:
                line = data_file.readline()
                while line:
                    s = line.split('\t')
                    if len(s) > 1:
                        yield s[1]
                    line = data_file.readline()



class Sentences_Parser_2(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __iter__(self):

        with open(self.file_name, "r", newline='') as data_file:
                line = data_file.readline()
                while line:
                    s = line.split('\t')
                    if len(s) > 1:
                        yield s[1].split()
                    line = data_file.readline()



class Sentences_Parser(object):
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.ignored_lines_count = 0
        self.total_lines = 0
        self.total_number_of_words = 0

        self.Match_Case_1 = re.compile(r'((\w*[\w\s])\/([\w\s]\w*))')                    #for words connected wby /
        self.Match_Case_2 = re.compile(r'([\s|^][a-z]{2,4}[\d|\s]\d{1,4})[\s|.]')      #for equipment ids
        self.Match_Case_3 = re.compile(r'\s[0-9]{2}/[0-9]{2}/[0-9]{2,4}')              #for datatiem format


    def Process_short_text(self, short_text):
        short_text = '  ' + short_text + '  '                                          # append whitespace at the back and front for easy of regex matching
        short_text = re.sub('&', ' and ', short_text)
        short_text = re.sub('@', ' at ', short_text)
        short_text = re.sub('\[', ' ', short_text)                                   #[safas] get rid of brackets
        short_text = re.sub('\]', ' ', short_text)                                   #[safas] get rid of brackets
        short_text = re.sub('re-', 're', short_text)                                # change re-kit to 'rekit'
        short_text = re.sub('-', ' ', short_text)
        short_text = re.sub('no.[\d|\s]\d+', ' number ', short_text)
# ------------------------third match Case---------------------------------------------------------------------------------------------------------------
        short_text = re.sub(self.Match_Case_3.pattern, ' date_time ', short_text)
#-------------------------First Case---------------------------------------------------------------------------------------------------------------
        # found_string_list = self.Match_Case_1.findall(short_text)
        # for found_string in found_string_list:
        #     if len(found_string) > 7:
        #         short_text = re.sub('\w\/\w', found_string[0].replace('/', ' '), short_text)
        #     if len(found_string) > 0 and len(found_string) < 7:
        #         short_text = re.sub('\w\/\w', found_string[0].replace('/', '_'), short_text)
        found_string_list = self.Match_Case_1.findall(short_text)
        for found_string in found_string_list:
            t0 = found_string[1].strip()
            t1 = found_string[2].strip()
            if len(t0) + len(t1) > 7:
                string_to_replace = t0 + ' ' + t1
            else:
                string_to_replace = t0 + '_' + t1
            #print(string_to_replace)
            short_text = re.sub(self.Match_Case_1.pattern, string_to_replace, short_text)

#-------------------------Second Case---------------------------------------------------------------------------------------------------------------
        short_text = re.sub(self.Match_Case_2.pattern ,' equipment_id ' , short_text )

        short_text = re.sub(r"'+", '', short_text)
        short_text = re.sub('\d+', '_number_', short_text)
        short_text = re.sub('[^_\w]+', ' ', short_text)    #replace charter other than '_'


#--------------------------Speacial Cases---------------------------------------------------------------------------------------------------
        short_text = re.sub('pos_number_', ' pos _number_  ', short_text)

        short_text = re.sub('(edd[_|_\s|\s_]number_)', ' equipment_id ', short_text)  # replace 'edd_number_' as 'equipment_id'
        short_text = re.sub('edd _number_', ' equipment_id ', short_text)  # replace 'edd _number_' as 'equipment_id'
        short_text = re.sub('(tkd[_|_\s|\s_]number_)', ' equipment_id ',short_text)  # replace 'edd_number_' as 'equipment_id'
        short_text = re.sub('tkd _number_', ' equipment_id ', short_text)  # replace 'edd _number_' as 'equipment_id'
        short_text = re.sub(r'(she(\s_|_)number_)', ' equipment_id ',short_text)  # replace 'she_number_' as 'equipment_id'
        short_text = re.sub(r'(exd(\s_|_|l_)number_)', ' equipment_id ',short_text)  # replace 'she_number_' as 'equipment_id'
        short_text = re.sub(r'(tkw(\s_|_)number_)', ' equipment_id ',short_text)  # replace 'she_number_' as 'equipment_id'
        short_text = re.sub(r'(shd(\s_|_)number_)', ' equipment_id ',short_text)  # replace 'she_number_' as 'equipment_id'
        short_text = re.sub(r'(trd(\s_|_)number_)', ' equipment_id ', short_text)  # replace 'edd_number_' as 'equipment_id'

        short_text = re.sub('grd_number_', ' equipment_id ', short_text)  # replace 'edd _number_' as 'equipment_id'
        short_text = re.sub(r'(rd(\s_|_)number_)', ' equipment_id ',short_text)  # replace 'edd_number_' as 'equipment_id'

        short_text = re.sub('\sr and r\s', ' r_r ', short_text)                   # replace 'r and r' as 'r_r'
        short_text = re.sub('\sr and i\s', ' r_i ', short_text)                   # replace 'r and i' as 'r_r'
        short_text = re.sub('\sp and t\s', ' p_t ', short_text)  # replace 'r and i' as 'r_r'
        short_text = re.sub('\sp and h\s', ' p_h ', short_text)  # replace 'r and i' as 'r_r'

        short_text = re.sub('_number_wk', ' _number_ week ', short_text)
        short_text = re.sub('_number_yr', ' _number_ yearly ', short_text)
        short_text = re.sub('wk_number_', 'week _number_ ', short_text)
        short_text = re.sub('_number_wkly', ' _number_ weekly ', short_text)
        short_text = re.sub('_number_mth', ' _number_ month ', short_text)
        short_text = re.sub('_number_m', ' _number_ month ', short_text)
        short_text = re.sub('_number_hr[\s|s]', ' _number_ hour ', short_text)
        short_text = re.sub('_number_hour', ' _number_ hour ', short_text)
        short_text = re.sub('_number_h ', ' _number_ hour ', short_text)
        short_text = re.sub('_number_min[\s|s] ', ' _number_ hour ', short_text)
        short_text = re.sub('_number_sec ', ' _number_ sec ', short_text)

        short_text = re.sub(' _number_x(?![_x])', ' _number_ x ', short_text)

        short_text = re.sub('_number_kg ', ' _number_ kg ', short_text)
        short_text = re.sub('_number_v ', ' _number_ volts ', short_text)
        short_text = re.sub('_number_w', ' _number_ watts ', short_text)
        short_text = re.sub('_number_kw', ' _number_ kilowatts ', short_text)

        short_text = re.sub('model_number_', 'model _number_ hour ', short_text)
        short_text = re.sub('manufacturer_number_', 'manufacturer _number_ hour ', short_text)

        short_text = re.sub('\s_number_st\s', ' first ', short_text)
        short_text = re.sub('\s_number_nd\s', ' second ', short_text)

#------------------------------Speacial Case 2----------------------------------------------------------------------------------------------------------------

        short_text = re.sub('\swill not\s',   ' cannot ', short_text)
        short_text = re.sub('wont\s',         ' cannot ', short_text)
        short_text = re.sub('won t\s',        ' cannot ', short_text)

        short_text = re.sub('cant\s',         ' cannot ', short_text)
        short_text = re.sub('can t\s',        ' cannot ', short_text)
        short_text = re.sub('\scan not\s',    ' cannot ', short_text)

        short_text = re.sub('\scould not\s',  ' cannot ', short_text)
        short_text = re.sub('\scouldnt\s',    ' cannot ', short_text)
        short_text = re.sub('\scouldn t\s',   ' cannot ', short_text)

        short_text = re.sub('\swould not\s', ' cannot ', short_text)
        short_text = re.sub('\swouldnt\s',     ' cannot ', short_text)
        short_text = re.sub('wouldn t\s',     ' cannot ', short_text)

        short_text = re.sub('over haul\s', ' overhaul ', short_text)
        short_text = re.sub('change out\s', ' changeout ', short_text)
        short_text = re.sub('up grade\s', ' upgrade ', short_text)
        short_text = re.sub('u s\s', ' u_s ', short_text)
        return short_text

    def __iter__(self):

        with open(self.dir_name + 'loader_work_orders_sanitised.csv', newline='') as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                self.total_lines+=1
                short_text = row[4]
                # only process if contains space, to get rid of the records where there is no space seperation
                if short_text.find(' ') > 0 :
                    short_text = self.Process_short_text(short_text)
                    yield short_text.split()
                else:
                    self.ignored_lines_count+=1

def Print_Out_Resuls(sentences):
    with open("../Data_Cleaning/Cleaned_Data_14.txt", "w") as cleaned_data_file:
        i = 1
        for sentence in sentences:
            string_to_print = str(i) + '\t' + " ".join(sentence)
            print( string_to_print , file=cleaned_data_file)
            i = i +1

        print('*******************************************************************************', file=cleaned_data_file)
        string_to_print = 'Total:' + str(sentences.total_lines) + '\t' + 'Ignored:' + str(sentences.ignored_lines_count)
        print(string_to_print, file=cleaned_data_file)


def Print_Out_Token_Frequecy(sentences):
    frequency = defaultdict(int)
    for sentence in sentences:
        for word in sentence:
            frequency[word] += 1
            sentences.total_number_of_words+=1
    i = 1
    with open("../Data_Cleaning/Cleaned_Data_Frequency_14.txt", "w") as cleaned_data_file:
        for w in sorted(frequency, key=frequency.get, reverse=True):
            string_to_print = str(i) + '\t' + w +'\t\t\t\t\t'+ str(frequency[w])
            print( string_to_print , file=cleaned_data_file)
            i+=1
        print('*******************************************************************************', file=cleaned_data_file)
        string_to_print = 'Total:' + str(sentences.total_number_of_words)
        print(string_to_print, file=cleaned_data_file)
    return frequency

def Build_Frequency_Dic(sentences):
    frequency = defaultdict(int)
    for sentence in sentences:
        for word in sentence:
            frequency[word] += 1
    return frequency

if __name__ == "__main__":
    sentences = Sentences_Parser('../Data_Set/')
    #sentences = Sentences_Parser_2('../Data_Cleaning/Cleaned_Data_11.txt')
    #for s in sentences:
       #print(s)
    Print_Out_Resuls(sentences)
    Print_Out_Token_Frequecy(sentences)