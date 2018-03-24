import nltk

text = nltk.word_tokenize("feed control not working")
print(nltk.pos_tag(text))


text = nltk.word_tokenize("repair cracked feed pipe")
print(nltk.pos_tag(text))


text = nltk.word_tokenize("propel pumps need neutralizing")
print(nltk.pos_tag(text))

text = nltk.word_tokenize("NA carousel and head feed problem")
print(nltk.pos_tag(text))

text = nltk.word_tokenize("fit 4 new tubeless tyres to rear of driv")
print(nltk.pos_tag(text))