import gensim
from Data_Preprocessing import Sentences_Parser_2
from Data_Preprocessing import Sentences_Parser

from nltk.cluster import KMeansClusterer
import nltk

import gensim

def write_vacab_to_txt(words):
    with open("../Ignored_Files/vacab_2.txt", "w") as vacab_file:
        i = 1
        for word in words:
            print(word + '\t\t ' + str(i), file = vacab_file)
            i = i + 1

if __name__ == "__main__":
    #sentences = Sentences_Parser('../Data_Set/')  # a memory-friendly iterator
    sentences = Sentences_Parser_2('../Data_Cleaning/Cleaned_Data_13s.txt')
    window_size = 5
    min_count = 2
    iteration_number = 200
    vector_size = 300
    threads_number = 4
    skim_gram = 1
    CBOW      = 0

    model = gensim.models.Word2Vec(sentences,sg = CBOW ,window=window_size,min_count= min_count,iter=iteration_number,size=vector_size,workers=threads_number)
    model.save('../Data_Set/mymodel_13')


    # model = gensim.models.Word2Vec.load('../Data_Set/mymodel_9')
    # X = model[model.wv.vocab]
    #
    # for i in range(5, 20):
    #     NUM_CLUSTERS = i
    #     kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.euclidean_distance, repeats= 100 )
    #     assigned_clusters = kclusterer.cluster(X, assign_clusters=True)
    #
    #     words = list(model.wv.vocab)
    #     with open("../Ignored_Files/Model_8_vacab_eulidien_" + str(i) + ".txt", "w") as vacab_file:
    #         for i, word in enumerate(words):
    #             print(word + "\t\t\t" + str(assigned_clusters[i]), file=vacab_file)




