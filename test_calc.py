from calc import add, celsiusToFahrenheit, oddOrEven

def test_add():
    assert add(2,3) == 5
    assert add(1,1) == 2
    assert add(10,2) == 12

def test_celsiusToFahrenheit():
    assert celsiusToFahrenheit(20) == 68
    assert celsiusToFahrenheit(35) == 95

def test_oddOrEven():
    assert oddOrEven(12) == False
    assert oddOrEven(3) == True
