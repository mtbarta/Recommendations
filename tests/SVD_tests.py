
test_tuples = [(1,1,3),
               (2,1,2),
               (1,2,5),
               (4,4,1)]

from src.algorithms.SVD import SVD
def test_SVD_init():
    svd = SVD(test_tuples, 4, 5, 5, .035, .001)
    print svd.U.shape
    print svd.V.shape
    assert svd.U.shape == (4,5)
    assert svd.V.shape == (5,5)

test_SVD_init()

svd = SVD(test_tuples, 4, 5, 5, .035, .001)
def test_SVD():
    svd.train(10)
    print svd.predict(0,2)

test_SVD()

from src.algorithms.SVD_gradients import SVD_gradients
def test_SVD_gradients():
    svd_grad = SVD_gradients(test_tuples, 4,5,5,.02,.001,.002)
    svd_grad.train(1)
    print "prediction for user 0, item 2 : %s" % svd_grad.predict(1,2)
    print "model RMSE: %s " % svd_grad.RMSE

    
test_SVD_gradients()
