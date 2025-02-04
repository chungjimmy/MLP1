# following https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

#print(dataset.head(20))
#print(dataset.describe())
#print(dataset.groupby('class').size())

#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
#dataset.hist()
#scatter_matrix(dataset)
#plt.show()

#split training data
array = dataset.values
x = array[:,0:4]
y = array[:,4]
xtrain, xvalid, ytrain, yvalid = train_test_split(x, y, test_size=0.20, random_state=1)

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, xtrain, ytrain, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
	
# Compare Algorithms
#plt.boxplot(results, labels=names)
#plt.title('Algorithm Comparison')
#plt.show()

#make predictions
model = SVC(gamma='auto')
model.fit(xtrain, ytrain)
predictions = model.predict(xtrain)

print(accuracy_score(ytrain, predictions))
print(confusion_matrix(ytrain, predictions))
print(classification_report(ytrain, predictions))

print("Success")