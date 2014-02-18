import numpy as np

test_tuples = [(0,0,3),
               (1,1,2),
               (0,2,5),
               (3,4,1)]

from src.utility import tuples_to_array

def test_tuples_to_array():
    target = np.matrix([[3,0,5,0,0],
                        [0,2,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,1]])
    val = tuples_to_array(test_tuples).todense() 
    
    np.testing.assert_array_equal(val,target, "The selected tuple data has accurately translated to a matrix")

