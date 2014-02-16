#Author: Matt Barta
# will need two types: real-time and stored
class RecommendationEngine():
    def __init__(self, data, metric = 'pearson', n = 5):
        