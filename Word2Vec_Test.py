import gensim
from sklearn.decomposition import PCA
from matplotlib import pyplot


def write_vacab_to_txt(words):
    with open("../Ignored_Files/vacab_1.txt", "w") as vacab_file:
        i = 1
        for word in words:
            print(word + '\t\t ' + str(i), file=vacab_file)
            i = i + 1


model = gensim.models.Word2Vec.load('../Data_Set/mymodel_1')

words = sorted(list(model.wv.vocab))
write_vacab_to_txt(words)

X = model[model.wv.vocab]

# pca = PCA(n_components=2)
# result = pca.fit_transform(X)
# # create a scatter plot of the projection
# pyplot.scatter(result[:, 0], result[:, 1])
# words = list(model.wv.vocab)
# for i, word in enumerate(words):
#     if not any(char.isdigit() for char in word) :
#         pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
#
# pyplot.show()
