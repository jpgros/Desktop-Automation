import pytest
import time
import Sources.Gui as Gui
import Sources.TestResources as tc
from unittest.mock import patch
from unittest.mock import Mock
#Carefull ptyesy-mock package need to be installed
# into pycharm to use mocker in tests

#put 'test' before each method name eather it will be ignored

@pytest.mark.greattoto
def testMock():
    print("test long begining")
    expected =123
    actual = expensive_api()
    assert actual==expected

@pytest.mark.greattoto
def test_use_case():
    print("begin manual test")
    g1 = Gui.Gui()
    g1.launchWindow()



@pytest.mark.testmock
def test_my_mock():
    mock = Mock()

@pytest.mark.testmock
def test_mock_app(mocker):
    mock_api = mocker.MagicMock(name='api')
    mocker.patch('main.addition', new=mock_api)
    result = tc.addition(2,3)
    assert result==5

@pytest.mark.testmock
def test_my_method_alternative():
    with patch('main.expensive_api_call',return_value=123) as patched_time_sleep:
        assert patched_time_sleep()==123

@pytest.fixture(scope="class")
def testInit():
    return 5

@pytest.mark.skip
def testMain(testInit):
    #assert main.toto()==4
    assert testInit == 5
    #g1 = Gui.Gui()
    #g1.launchWindow()

@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100

@pytest.mark.less
def test_less():
    num = 100
    assert num < 200

@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0

@pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 35), (4, 44)])
def test_multiplication_11(num, output):
    assert 11 * num == output

def expensive_api():
    time.sleep(1)
    return 123