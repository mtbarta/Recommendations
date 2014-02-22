import numpy as np
import math
# implement biases-- http://arek-paterek.com/ap_kdd_poster.pdf
# gradients -- http://www.csie.ntu.edu.tw/~r95007/thesis/svdnetflix/report/report.pdf
class SVD():
    def __init__(self, data, user_count, item_count, rank, learning_rate, reg_users, reg_items):
        """data is a tuple of tuples (user, item, rating)"""
        self.data = data
        self.rank = rank #factors
        self.user_count = user_count
        self.item_count = item_count
        self.learning_rate = learning_rate
        self.reg_users = reg_users
        self.reg_items = reg_items
        self.minimprove = .0001
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
        prediction = 0 
        for i in range(self.rank):
            prediction += self.U[userid][i] * self.V[itemid][i]
        return prediction
        
    def train(self, epochs):
        oldtrain = 0
        for epoch in range(epochs):
            train = self.train_single(self.rank -1)
            
            if abs(oldtrain - train) < self.minimprove:
                break
            oldtrain = train
            
        
    def train_single(self, k):
        """iterate through the data. For each rating, update the user and item factors."""
        
        for userid, item, rating in self.data:
            itemid = item-1 # should not be hard coded
            
            error = .5 * (rating - self.predict(userid, itemid))**2 + \
                    self.reg_users*.5*sum([i**2 for i in self.U[userid]]) + \
                    self.reg_items*.5*sum([i**2 for i in self.V[itemid]])
            
            
            u_gradient = (rating - self.predict(userid,itemid)) * self.V[itemid] - \
                        self.U[userid] * self.reg_users
            v_gradient = (rating - self.predict(userid,itemid)) * self.U[userid] - \
                        self.V[itemid] * self.reg_items
            
            self.U[userid] -= self.learning_rate * u_gradient
            self.V[itemid] -= self.learning_rate * v_gradient
            
        return math.sqrt(error / len(self.data))
            