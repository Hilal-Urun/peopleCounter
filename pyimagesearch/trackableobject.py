# to track and count an object in a video need to store info regarding to obj itself (objectID, previous centroids, object has already counted or not)

class TrackableObject:
    def __init__(self, objectID, centroid):
        # store the object ID, then initialize a list (because contains loc hist) of centroids
        # using the current centroid
        self.objectID = objectID
        self.centroids = [centroid]
        # initialize a boolean used to indicate if the object has
        # already been counted or not
        self.counted = False
