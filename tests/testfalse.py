#the following test all fail
def test_assert_false():
    assert False

def test_assert_int_value_inequality():
    x=3
    y=4
    assert x==y

def test_assert_int_value_inequality():
    x=4.1
    y=4
    assert x==y

def test_assert_int_value_inequality():
    x=True
    y=3 == 4 
    assert x==y