class Algorithm(object):
    """abstract class to define an algorithm"""
    def train(self):
        pass
    def predict(self, userid, itemid):
        pass
    def validate(self, test_data):
        """determine RMSE on test set"""
        Sqerror = 0
        for user,item, rating in test_data:
            Sqerror += (rating - self.predict(user,item))**2
        return Sqerror / len(test_data)