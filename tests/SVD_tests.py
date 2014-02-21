
test_tuples = [(0,1,3),
               (1,1,2),
               (0,2,5),
               (3,4,1)]

from src.SVD import SVD
def test_SVD_init():
    """TODO assert U and V are of correct size"""
    svd = SVD(test_tuples, 4, 5, 5, .035, .001)
    assert svd.U.shape == (5,5)
    assert svd.V.shape == (4,5)

svd = SVD(test_tuples, 4, 5, 5, .035, .001)
def test_SVD():
    svd.train(10, 10)
    print svd.predict(0,2)

test_SVD()