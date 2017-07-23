import random
import math


NUM_CLUSTERS = 4
TOTAL_DATA = 15
LOWEST_SAMPLE_POINT = 0 #element 0 of SAMPLES.
HIGHEST_SAMPLE_POINT = 14 #element 3 of SAMPLES.
BIG_NUMBER = math.pow(10, 10)
COUNTER=0
isStillMoving=2

SAMPLES = [[1.0,1.0],[1.0,2.0],[2.0,0],[2.0,3.0],[5.0,10.0],[5.0,12.0],[6.0,2.0],[6.0,4.0],[6.0,10.0],[7.0,2.0],[7.0,5.0],[9.0,9.0],[10.0,7.0],[10.0,9.0],[11.0,8.0]]

data = []
centroids = []

class DataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_x(self, x):
        self.x = x
    
    def get_x(self):
        return self.x
    
    def set_y(self, y):
        self.y = y
    
    def get_y(self):
        return self.y
    
    def set_cluster(self, clusterNumber):
        self.clusterNumber = clusterNumber
    
    def get_cluster(self):
        return self.clusterNumber

class Centroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_x(self, x):
        self.x = x
    
    def get_x(self):
        return self.x
    
    def set_y(self, y):
        self.y = y
    
    def get_y(self):
        return self.y

def initialize_centroids():
    # Set the centoid coordinates to match the data points furthest from each other.
    # In this example, (1.0, 1.0) and (5.0, 7.0)
    centroids.append(Centroid(SAMPLES[0][0], SAMPLES[0][1]))
    centroids.append(Centroid(SAMPLES[4][0], SAMPLES[4][1]))
    centroids.append(Centroid(SAMPLES[6][0], SAMPLES[6][1]))
    centroids.append(Centroid(SAMPLES[11][0], SAMPLES[11][1]))
    
    print("Centroids initialized at:")
    print("(", centroids[0].get_x(), ", ", centroids[0].get_y(), ")")
    print("(", centroids[1].get_x(), ", ", centroids[1].get_y(), ")")
    print("(", centroids[2].get_x(), ", ", centroids[2].get_y(), ")")
    print("(", centroids[3].get_x(), ", ", centroids[3].get_y(), ")")
    print()
    return

def initialize_datapoints():
    # DataPoint objects' x and y values are taken from the SAMPLE array.
    # The DataPoints associated with LOWEST_SAMPLE_POINT and HIGHEST_SAMPLE_POINT are initially
    # assigned to the clusters matching the LOWEST_SAMPLE_POINT and HIGHEST_SAMPLE_POINT centroids.
    for i in range(TOTAL_DATA):
        newPoint = DataPoint(SAMPLES[i][0], SAMPLES[i][1])
        
        if(i == 0):
            newPoint.set_cluster(0)
        elif(i == 4):
            newPoint.set_cluster(1)
        elif(i == 6):
            newPoint.set_cluster(2)
        elif(i == 11):
            newPoint.set_cluster(3)
        else:
            newPoint.set_cluster(None)
            
        data.append(newPoint)
    
    return

def get_distance(dataPointX, dataPointY, centroidX, centroidY):
    # Calculate Euclidean distance.
    return math.sqrt(math.pow((centroidY - dataPointY), 2) + math.pow((centroidX - dataPointX), 2))

def recalculate_centroids():

    for j in range(NUM_CLUSTERS):
        totalX = 0
        totalY = 0
        totalInCluster = 0
        for k in range(len(data)):
            if(data[k].get_cluster() == j):
                print("data "+str(k)+"in cluster"+str(j))
                totalX += data[k].get_x()
                totalY += data[k].get_y()
                totalInCluster += 1
        
        if(totalInCluster > 0):
            centroids[j].set_x(totalX / totalInCluster)
            centroids[j].set_y(totalY / totalInCluster)
            print("Total in Cluster"+str(totalInCluster))
            print("recalculate centroid of cluster"+str(j))
            print("(", centroids[j].get_x(), ", ", centroids[j].get_y(), ")")
    
    return

def update_clusters():
    global isStillMoving
    global COUNTER
    COUNTER +=1
    print("update counter= "+str(COUNTER))
    isStillMoving -=1
    for i in range(TOTAL_DATA):
        bestMinimum = BIG_NUMBER
        currentCluster = 0
        
        for j in range(NUM_CLUSTERS):
            distance = get_distance(data[i].get_x(), data[i].get_y(), centroids[j].get_x(), centroids[j].get_y())
            if(distance < bestMinimum):
                bestMinimum = distance
                currentCluster = j
        
        data[i].set_cluster(currentCluster)
        
        if(data[i].get_cluster() is None or data[i].get_cluster() != currentCluster):
            data[i].set_cluster(currentCluster)
            isStillMoving = 1
    
    return isStillMoving

def perform_kmeans():
    isStillMoving = 1

    initialize_centroids()
    
    initialize_datapoints()
    
    while(isStillMoving):
        recalculate_centroids()
        isStillMoving = update_clusters()
    
    return

def print_results():
    for i in range(NUM_CLUSTERS):
        print("Cluster ", i, " includes:")
        for j in range(TOTAL_DATA):
            if(data[j].get_cluster() == i):
                print("(", data[j].get_x(), ", ", data[j].get_y(), ")")
        print()
    
    return

perform_kmeans()
print_results()