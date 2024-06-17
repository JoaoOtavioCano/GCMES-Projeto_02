from backend.login import Login, __createAuthenticationKey__

def test__createAuthenticationKey__():
    userID = 1
    authKey = __createAuthenticationKey__(userID)

    assert authKey.find('#') == 10
    assert len(authKey) == 75
    assert authKey.split('#', 1)[0] == "0000000001"
