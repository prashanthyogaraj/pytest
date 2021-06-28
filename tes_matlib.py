import matlib
import pytest



@pytest.mark.parametrize("a,b,out",[(2,3,5),(5,3,8)])	
def test_cal_sum(a,b,out):
    print(a,b)
    total = matlib.cal_sum(a,b)
    assert total == out
	
@pytest.mark.skip
@pytest.mark.check
def test_cal_mul():
    total=matlib.cal_mul(2,3)
    assert total == 6
	
def test_sub():
    out=matlib.te_sub(3,2)
    assert out == 1
	

def test_find_odd(input_func):
    assert input_func%3==0