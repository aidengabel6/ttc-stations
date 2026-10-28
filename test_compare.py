import pytest
import compare

def test_compare():
    assert compare.minimum(1,2) == 1
    assert compare.minimum(2,1) == 1
    assert compare.minimum(1,1) == 1

