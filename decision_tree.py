#-------------------------------------------------------------------------
# AUTHOR: Jeremiah Garcia
# FILENAME: decision_tree.py
# SPECIFICATION: this program processes an input file into a decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: 2 Hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = [[0 for i in range(4)] for j in range(10)]
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
   reader = csv.reader(csvfile)
   for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append(row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =

# I would have prefered to seperate the original data into X and Y in one section instead of two but because the assignment
# Separated it I will do it in two separate passes
for i, row in enumerate(db):
    for j, column in enumerate(row):
        if j == 4:
            continue

        if column == "Young":
            X[i][j] = 1
        elif column == "Prepresbyopic":
            X[i][j] = 2
        elif column == "Presbyopic":
            X[i][j] = 3
        elif column == "Myope":
            X[i][j] = 1
        elif column == "Hypermetrope":
            X[i][j] = 2
        elif column == "Yes":
            X[i][j] = 1
        elif column == "No":
            X[i][j] = 2
        elif column == "Reduced":
            X[i][j] = 1
        elif column == "Normal":
            X[i][j] = 2
        else:
            X[i][j] = 0



#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =

for i, row in enumerate(db):
    for j, column in enumerate(row):
        if j != 4:
            continue

        if column == "Yes":
            Y.append(1)
        elif column == "No":
            Y.append(2)
        else:
            Y.append(0)


#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes', 'No'], filled=True, rounded=True)
plt.show()
