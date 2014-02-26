
test_tuples = [(0,1,3),
               (1,1,2),
               (0,2,5),
               (3,4,1)]

from src.SVD import SVD
def test_SVD_init():
    svd = SVD(test_tuples, 4, 5, 5, .035, .001)
    assert svd.U.shape == (5,5)
    assert svd.V.shape == (4,5)

svd = SVD(test_tuples, 4, 5, 5, .035, .001)
def test_SVD():
    svd.train(10)
    print svd.predict(0,2)

from src.SVD_gradients import SVD_gradients
def test_SVD_gradients():
    svd_grad = SVD_gradients(test_tuples, 4,5,5,.02,.001,.002)
    svd_grad.train(1)
    print "prediction for user 0, item 2 : %s" % svd_grad.predict(0,2)
    print "model RMSE: %s " % svd_grad.RMSE

    
test_SVD_gradients()
