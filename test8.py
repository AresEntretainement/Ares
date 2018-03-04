import pickle

clf = LinearRegression()
with open('algorithmefile.picke', 'wb') as f:
	pickle.dump(clf,f)

pickle_in = open('algorithmefile.picke','rb')
clf = pickle.load(pickle_in)