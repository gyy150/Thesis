from nltk.cluster import KMeansClusterer
import nltk

import gensim

def write_vacab_to_txt(words):
    with open("../Ignored_Files/vacab_2.txt", "w") as vacab_file:
        i = 1
        for word in words:
            print(word + '\t\t ' + str(i), file = vacab_file)
            i = i + 1

model = gensim.models.Word2Vec.load('../Data_Set/mymodel_2')
X = model[model.wv.vocab]

for i in range(10,20):
    NUM_CLUSTERS = i
    kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats = 25 )
    assigned_clusters = kclusterer.cluster(X, assign_clusters=True)

    words = list(model.wv.vocab)
    with open("../Ignored_Files/vacab_"+str(i)+".txt", "w") as vacab_file:
        for i, word in enumerate(words):
            print(word + "\t\t\t" + str(assigned_clusters[i]), file=vacab_file)

