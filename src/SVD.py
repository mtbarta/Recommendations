import numpy as np


class SVD():
    def __init__(self, data, user_count, item_count, rank, learning_rate, reg):
        """data is a tuple of tuples (user, item, rating)"""
        self.rank = rank
        self.user_count = user_count
        self.item_count = item_count
        self.learning_rate = learning_rate
        self.reg = reg
        #create average rating for initial values
        average = np.average([line[2] for line in data])
        init = np.sqrt(average/rank)
        noise = .005
        
        self.U = np.random.RandomState.uniform(-noise, noise, item_count*rank)\
                .reshape(item_count,rank) + init
        self.V = np.random.RandomState.uniform(-noise,noise, user_count*rank)\
                .reshape(user_count, rank) + init
    @classmethod
    def train(cls, data, epochs):
        