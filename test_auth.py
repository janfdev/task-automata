from auth import login

def test_login_berhasil():
    assert login("admin", "12345") == True

def test_username_salah():
    assert login("user", "12345") == False

def test_password_salah():
    assert login("admin", "00000") == False
