import gensim
from Data_Preprocessing import Sentences_Parser

if __name__ == "__main__":
    sentences = Sentences_Parser('../Data_Set/')  # a memory-friendly iterator

    ##for s in sentences:
    ##    print(s)

    model = gensim.models.Word2Vec(sentences , min_count= 2 ,  size=200 ,  workers=4)
    model.save('../Data_Set/mymodel_3')

