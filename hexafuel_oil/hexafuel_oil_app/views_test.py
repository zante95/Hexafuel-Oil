from views import home

def test_home():
    assert home(request) == (request, 'hexafuel_oil_app/login.html')