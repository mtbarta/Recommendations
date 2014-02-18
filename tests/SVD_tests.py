
test_tuples = [(0,0,3),
               (1,1,2),
               (0,2,5),
               (3,4,1)]

from src.SVD import SVD
def test_SVD_init():
    """TODO assert U and V are of correct size"""
    svd = SVD(test_tuples, 4, 5, 5, .035, .001)
    assert svd.U.shape == (5,5)
    assert svd.V.shape == (4,5)
    
