1. set number of clusters: 
	- UM_CLUSTERS: specify the number of clusters
2. input data samples
	- SAMPLES: Initialize array of samples by submitting each data point in the form of [x,y]
3. set number of epoch times
	- isStillMoving: specify the number of epoch, 
		if isStillMoving = 2, number of epoch =1,
		if isStillMoving = 3, number of epoch =2,
4. set initial seeds
	- set the initial seeds in
		- def "initialize_datapoint" , set_cluster()
		- def "initialize_centroids" , centroids.append

5. Execute
	- clustering.py 
		- to get the cluster distribution and new cluster center generated in each epoch
	- new_initialSeeds.py
	 	- to get the new cluster distribution and new cluster center generated in each epoch with new initial seeds