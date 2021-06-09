import calculator as cal

def test_multiply():
    result = cal.multiply(3,3)
    assert result==9

def test_multiply_zero():
    result = cal.multiply(3,0)
    assert result==0

def test_multiply_neg_number():
    result = cal.multiply(3,-3)
    assert result==-9