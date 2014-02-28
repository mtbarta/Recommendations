import scipy.sparse as sparse

def tuples_to_dict(data):
    """starting with (userid,itemid, rating), create a ratings array"""
    array = []
    for user,item,rating in data:
        array.setdefault(user,{})
        array[user][item] = rating
        
def tuples_to_array(data):
    """from (userid,itemid, rating), return a scipy coo sparse matrix)"""
    user = [line[0] for line in data]
    item = [line[1] for line in data]
    rating = [line[2] for line in data]
        
    return sparse.coo_matrix((rating, (user,item)))

