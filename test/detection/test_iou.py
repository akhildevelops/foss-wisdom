from wisdom.retail import common_area
import numpy as np
def test_iou():
    a = np.array([[0,5,5,10]])
    b = np.array([[1,1,3,3]])
    intersection = common_area(a,b)
    assert intersection==None

    a = np.array([[0,5,5,10]])
    b = np.array([[1,1,3,7]])
    intersection = common_area(a,b)
    assert intersection[0]-0.12<0.01