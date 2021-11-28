import pytest
#import requests

def lessThan5(test_input):
    if test_input < 6:
        return True
    else:
        return False
    return True

#pytest.mark.parametrize는 이거 선언한 바로 아래 test에만 적용되는 것으로 보인다.
@pytest.mark.parametrize("input,result", [
    (1, True),
    (2, True),
    (3, True),
    (6, False),
    (7, False)
])
def test_lessThan5(input, result):
    assert lessThan5(input) == result
    
# @pytest.mark.parametrize("x", [0, 1])
# @pytest.mark.parametrize("y", [2, 3, 4])
# def test_foo(x, y):
#     #pass
#     assert x*y == x*2