from nltk.corpus import words as Legal_Words
from Data_Preprocessing import Words_Parser
from nltk.stem.wordnet import WordNetLemmatizer

Lem = WordNetLemmatizer()

def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in Legal_Words.words())

def variants(word):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    """get all possible variants for a word"""
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts    = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def Check_1(word):
    lemmatized_word = Lem.lemmatize(word)
    return lemmatized_word


def Check_2(word):
    return known(variants(word))

def Print_lemmatized_word(dir_name, file_name):
    words = Words_Parser(dir_name,file_name)
    with open("../Data_Cleaning/lemmatized_word_4.txt", "w") as lemmatized_word_file:
        i = 1
        for word in words:
            line_new = '{:<3}  {:<42}  {:<42}  {:<42}'.format(str(i), word, Check_1(word), (Check_1(word) in Legal_Words.words()))
            print( line_new , file=lemmatized_word_file)
            i = i +1


def Print_Corrected_Words(dir_name, file_name):
    words = Words_Parser(dir_name, file_name)
    with open("../Data_Cleaning/lemmatized_word.txt", "w") as lemmatized_word_file:
        i = 1
        for word in words:
            if word not in Legal_Words.words():
                if word.find('_') < 0 :
                    print('\t'+word + '\t------')
                    print(Check_2(word))


if __name__ == "__main__":
    Print_lemmatized_word('../Ignored_Files/','vacab_4.txt')
    ##Print_Corrected_Words('../Ignored_Files/', 'vacab_3.txt')