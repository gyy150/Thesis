import gensim

model = gensim.models.Word2Vec.load('../Data_Set/mymodel_2')


#print(model['cable'])
#print(model['cables'])
print(model.most_similar(positive=['cabinets'], topn = 10))
print(model.most_similar(positive=['chec'], topn = 10))
print(model.most_similar(positive=['check'], topn = 10))
print(model.most_similar(positive=['lack'], topn = 10))
print(model.most_similar(positive=['leak'], topn = 10))
print(model.most_similar(positive=['fault'], topn = 10))
print(model.most_similar(positive=['fire'], topn = 10))
print(model.most_similar(positive=['finish'], topn = 10))
print(model.most_similar(positive=['fix'], topn = 10))
print(model.most_similar(positive=['broken'], topn = 10))
print(model.most_similar(positive=['ndt'], topn = 10))
print(model.most_similar(positive=['edd'], topn = 10))
print(model.most_similar(positive=['change'], topn = 10))
print(model.most_similar(positive=['wouldnt'], topn = 10))
print(model.most_similar(positive=['damage'], topn = 10))
print(model.most_similar(positive=['dmg'], topn = 10))
print(model.most_similar(positive=['and'], topn = 10))


print(model.similarity('cabinets', 'cabinet'))
print(model.similarity('camshafts', 'camshaft'))
print(model.similarity('cancelled', 'canceled'))
print(model.similarity('cannister', 'cannisters'))