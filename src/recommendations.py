#Author: Matt Barta


#may scrap in favor of a more open implementation
class RecommendationEngine():
    def __init__(self, data, algo):
        try:
            __import__("src.algorithms.{0}.{1}".format(algo, algo))

        except ImportError:
            print "Algorithm failed to load from src.algorithms. Make sure both"\
                    "file and class name match input"
        
        # TODO: split data into train and test.
    def data_split(self, train_ratio):
        