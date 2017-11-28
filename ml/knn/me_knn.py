import csv
import random
import math
import operator

#Loading our dataset
def dataload(file,split,train=[],test=[]):
    with open(file,'r') as csvfile:
        lines=csv.reader(csvfile)
        data=list(lines)

        #print(data)
        #for x in range(len(data)-1): #bug!!!!!!!!!!!
        # first line is label names
        for x in range(1,len(data)-1): #go through all rows
            for y in range(4):	#convert values to float from str
                data[x][y]=float(data[x][y])
            if(random.random()<split):
                train.append(data[x])
            else:
                test.append(data[x])


trainingSet=[] ; test=[]
split = 0.67

dataload('iris.csv', split, trainingSet, test)
print('Train set: ',len(trainingSet))
print('Test set: ',len(test))


def MinkowskiDistance(x1, x2, length, p):
    sum = 0
    for i in range(length):
        sum  += math.pow(abs(float(x1[i]) - float(x2[i])), 2 )
    return math.pow(sum, 1/2)
   
def Accuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
   
   
#Voting the classes obtained from Neighbours
def Response(neighbors):
	Votes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in Votes:
			Votes[response] += 1
		else:
			Votes[response] = 1
	sortedVotes = sorted(Votes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]


def Neighbors(train, test, p):
    distances = []
    length = len(test)-1	#Nof cols in each row, except last col which is label
    for x in range(len(train)):
        dist = MinkowskiDistance(test, train[x] , length, p )
        distances.append((train[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def compareDistance(trainingSet, test, k):
    for p in [1 , 2 , 6, 90]:
        predictions = []
        for x in range(len(test)):
            neighbors = Neighbors(trainingSet, test[x], p)
            result = Response(neighbors)
            predictions.append(result)
        accuracy = Accuracy(test, predictions)
        print("p:", p , accuracy)

#predictions=[]
k = 3
compareDistance(trainingSet, test, k)











