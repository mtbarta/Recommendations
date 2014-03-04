import numpy as np
from src.algorithms.algorithm import Algorithm
# implement biases-- http://arek-paterek.com/ap_kdd_poster.pdf
class SVD(Algorithm):
    def __init__(self, data, user_count, item_count, 
                 rank = 50, 
                 learning_rate = .001, 
                 reg = .05):
        """data is a tuple of tuples (user, item, rating)"""
        self.data = data
        self.rank = rank #factors
        self.user_count = user_count
        self.item_count = item_count
        self.learning_rate = learning_rate
        self.reg = reg
        self.minimprove = .0001
        self.RMSE = 0
        
        #create average rating for initial values
        average = np.average([line[2] for line in data])
        init = np.sqrt(average/rank)
        noise = .005
        
        #items
        self.V = np.random.uniform(-noise, noise, item_count*rank)\
                .reshape(item_count,rank) + init
        #users
        self.U = np.random.uniform(-noise,noise, user_count*rank)\
                .reshape(user_count, rank) + init
                
    def predict(self, userid, itemid):
        """rating of user i and item j is simply the dot product"""
        prediction = 0 #np.average(self.U[userid])
        for i in range(self.rank):
            prediction += self.U[userid-1][i] * self.V[itemid-1][i]
        return prediction
        
    def train(self, epochs = 20):
        print "starting training..."
        for epoch in range(epochs):
            print "training -- epoch: %s" % epoch
            train = self.train_single()
            print "..... RMSE: %s" % train
            if np.abs(self.RMSE - train) < self.minimprove:
                break
            self.RMSE = train
        
    def train_single(self):
        """iterate through the data. For each rating, update the user and item factors."""
        SSqerror = 0.0
        
        for user, item, rating in self.data:
            itemid = item-1
            userid = user -1
            
            error = rating - self.predict(user, item)
            SSqerror += error ** 2
            for rank in range(self.rank):
                uTemp = self.U[userid][rank]
                vTemp = self.V[itemid][rank]
                
                self.U[userid][rank] += self.learning_rate * (error * vTemp - self.reg * uTemp)
                self.V[itemid][rank] += self.learning_rate * (error * uTemp - self.reg * vTemp)
                
        return SSqerror / len(self.data)
            