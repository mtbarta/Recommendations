import numpy as np

# TODO: implement biases-- http://arek-paterek.com/ap_kdd_poster.pdf
# TODO: implement validation set training.
# gradients -- http://www.csie.ntu.edu.tw/~r95007/thesis/svdnetflix/report/report.pdf
from src.algorithms.SVD import SVD
class SVD_gradients(SVD):
    def __init__(self, data, user_count, 
                 item_count, rank = 50, 
                 learning_rate = .001, 
                 reg_users = .05, 
                 reg_items = .05):
        super(self.__class__, self).__init__(data, user_count, item_count, rank, learning_rate, reg = None)

        self.reg_users = reg_users
        self.reg_items = reg_items          
        
    def train_single(self):
        """iterate through the data. For each rating, update the user and item factors."""
        Sumerror = 0
        for user, item, rating in self.data:
            itemid = item-1 # should not be hard coded
            userid = user-1

            error = .5 * (rating - self.predict(user, item))**2 + \
                    self.reg_users*.5*np.linalg.norm(self.U[userid]) + \
                    self.reg_items*.5*np.linalg.norm(self.V[itemid])
            Sumerror += error
            u_gradient = (rating - self.predict(user,item)) * self.V[itemid] - \
                        self.U[userid] * self.reg_users
            v_gradient = (rating - self.predict(user,item)) * self.U[userid] - \
                        self.V[itemid] * self.reg_items
            
            self.U[userid] += self.learning_rate * u_gradient
            self.V[itemid] += self.learning_rate * v_gradient
            
        return np.sqrt(Sumerror / len(self.data))
            