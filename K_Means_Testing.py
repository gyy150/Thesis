from nltk.cluster import KMeansClusterer
import nltk
import copy
import gensim

def write_vacab_to_txt(words):
    with open("../Ignored_Files/vacab_2.txt", "w") as vacab_file:
        i = 1
        for word in words:
            print(word + '\t\t ' + str(i), file = vacab_file)
            i = i + 1


def cluster():
    model = gensim.models.Word2Vec.load('../Data_Set/mymodel_13')
    filtered_vocab = copy.deepcopy(model.wv.vocab)
    for word in model.wv.vocab.keys():
        if model.wv.vocab[word].count < 10:
            filtered_vocab.pop(word)

    X = model[filtered_vocab]

    for i in range(5,20):
        NUM_CLUSTERS = i
        kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats = 25 )
        assigned_clusters = kclusterer.cluster(X, assign_clusters=True)

        words = list(filtered_vocab)
        with open("../Ignored_Files/Model_13_vacab_eulidien_"+str(i)+".txt", "w") as vacab_file:
            for i, word in enumerate(words):
                print(word + "\t\t\t" + str(assigned_clusters[i]), file=vacab_file)

def display_result():
    with open("../Ignored_Files/vacab_2.txt", "r") as vacab_file:
        line = vacab_file.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1


if __name__ == '__main__':
    #display_result()
    cluster()

    