#author: Matt Barta
#info: Recommendation Engine
import data

def main():
    db = data.Database()
    db.connect(host="localhost", 
                 user= "",
                 passwd = "",
                 db = "recoDB")
    
    ratings = db.get_ratings()
    something = "smthng"
    print " some {0} , {1}".format(something, something)

if __name__ == "__main__":
    main()