from nltk import FreqDist
from Data_Preprocessing import Sentences_Parser_3

sentences = Sentences_Parser_3('../Data_Cleaning/Cleaned_Data_13.txt')
fdist = FreqDist(sentences)
fdist.plot()