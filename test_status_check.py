import status_check

# test status_check.mp_eligibility
def test_mp_eligibility():
    assert status_check.mp_eligibility(True, 20)
    assert not status_check.mp_eligibility(False, 70)
    assert not status_check.mp_eligibility(True, 17)
    assert status_check.mp_eligibility(True, 18)
    assert status_check.mp_eligibility(True, 1000)
    assert not status_check.mp_eligibility(False, 17)

# test status_check.sen_eligibility
def test_sen_eligibility():
    assert False