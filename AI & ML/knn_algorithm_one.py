# Open our dataset
import csv
with open(r"C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\iris_knn.data.txt") as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print(", ".join(row))



# Split our dataset
import csv
import random
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, "r") as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
                if random.random() < split:
                    trainingSet.append(dataset[x])
                else:
                    testSet.append(dataset[x])



# Load dataset
trainingSet = []
testSet = []
loadDataset(r"C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\iris_knn.data.txt", 0.66, trainingSet, testSet)
print(f"Train: {repr(len(trainingSet))}")
print(f"Test: {repr(len(testSet))}")



# Find the similiarities
import math
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)



# Test the distance function
data1 = [2, 2, 2, "a"]
data2 = [4, 4, 4, "b"]
distance = euclideanDistance(data1, data2, 3)
print(f"Euclidean Distance: {repr(distance)}")



# Get nearest neighbors
import operator
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors



# Test the get neighbors function
trainSet = [[2, 3, 2, "a"], [4, 4, 4, "b"]]
testInstance = [5, 5, 5]
k = 1
neighbors = getNeighbors(trainSet, testInstance, 1)
print(f"Neighbors: {neighbors}")



# Get the responses and votes
import operator
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]



# Test of get response function
neighbors = [[1, 1, 1, "a"], [2, 2, 2, "a"], [3, 3, 3, "b"]]
response = getResponse(neighbors)
print(f"Response: {response}")



# Accuracy evaluation
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] is predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0



# Test the accuracy function
testSet = [[1, 1, 1, "a"], [2, 2, 2, "a"], [3, 3, 3, "b"]]
predictions = ["a", "a", "a"]
accuracy = getAccuracy(testSet, predictions)
print(f"Accuracy: {accuracy}")


# Combine all functions in a function --> main
def main():
    # prepare data
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset("C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\iris_knn.data.txt", split, trainingSet,
                testSet)
    print(f"Train Set: {repr(len(trainingSet))}")
    print(f"Test Set: {repr(len(testSet))}")

    # generate predictions
    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print(f"> Predicted = {repr(result)}, Actual = {repr(testSet[x][-1])}")
    accuracy = getAccuracy(testSet, predictions)
    print(f"Accuracy: {repr(accuracy)}%")


main()