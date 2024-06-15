import pytest

from backend.authenticator import *


class FakeRequest:
    def __init__(self):
        self.headers = {}

@pytest.fixture
def authenticator():
    return Authenticator()

def test_validateAuthentication_01(authenticator):
    request = FakeRequest()
    request.headers["Cookie"] = "authenticationKey=00001#99999999999;"
    
    authenticator.authorization_list["00001"] = "00001#99999999999"
    
    assert authenticator.validateAuthentication(request) == True
