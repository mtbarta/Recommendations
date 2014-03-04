#author: Matt Barta
#info: Recommendation Engine
import data

def main():
    db = data.Database()
    db.connect(host="localhost", 
                 user= "recoDBuser",
                 passwd = "recopwd",
                 db = "recoDB")
    
    ratings = db.get_ratings()

    train = ratings[:85000]
    test = ratings[85000:]
    
    from src.algorithms.SVD_gradients import SVD_gradients
    from src.algorithms.SVD import SVD
    algo = SVD_gradients(train, 943, 1682, rank = 10)
    algo.train()
    print algo.validate(test)

if __name__ == "__main__":
    main()