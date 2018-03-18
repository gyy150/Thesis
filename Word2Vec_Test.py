import gensim
from sklearn.decomposition import PCA
from matplotlib import pyplot


model = gensim.models.Word2Vec.load('../Data_Set/mymodel')

words = sorted(list(model.wv.vocab))


X = model[model.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(model.wv.vocab)
for i, word in enumerate(words):
    if not any(char.isdigit() for char in word) :
        pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))

pyplot.show()


#with open("../Ignored_Files/vacab.txt", "w") as vacab_gile:
#    i = 1
#    for word in words:
#        print(word + '\t\t ' + str(i), file= vacab_gile)
#        i = i + 1


