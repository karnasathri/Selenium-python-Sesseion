import pytest

@pytest.mark.home
def test_m4():
    assert False

def test_m5():
    assert 100 == 100

@pytest.mark.home
def test_m6():
    assert "karna" == "KARNA"
@pytest.mark.home
def test_login_gmail():
    assert "admin" == "admin"