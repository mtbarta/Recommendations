import numpy as np


class SVD():
    def __init__(self, data, rank, learning_rate, reg):
        """TODO"""
        self.ratings = data
        self.num_users = data.shape(axis=0)
        self.num_features = data.shape(axis=1)
        
        #create average rating for initial values
        average = sum(data[2])
        init = np.sqrt(average/rank)
        
        self.U = 