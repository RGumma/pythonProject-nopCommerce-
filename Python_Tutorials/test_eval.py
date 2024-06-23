import pytest


@pytest.mark.parametrize("test_input, expected_output",[("3+5",8),("2+4",6),("6*9",42)])
def test_eval(test_input, expected_output):
    assert eval(test_input)==expected_output
#pytest.mark.parametrize decorator enables paramterization of arguments for a test function
#paramterize - performs multiple calls to the samefunction

#use fixture in class and modules  with use fixtures




@pytest.mark.skip
def add_number(a,b):
    c=a+b
    print(c)

add_number(2,3)

#the simplest way to skip a test function is to mark it with skip decorator

@pytest.mark.skip

@pytest.mark.skipif
# if you wish to skip something conditionally then you can use skipif instead.
#if the condition evaluates to true during collection the test function will be skipped

@pytest.mark.xfail
# you can use xfail marker to indicate that you expect a test to fail
# The test will run but no trace back will be reported when it fails






