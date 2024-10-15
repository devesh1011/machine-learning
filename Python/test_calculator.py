from calculator import add

def test_add():
    assert add(2, 4) == 6
    assert add(-1, 1) == 0
    assert add(-2, -2) == -4

# to test the code command to run in terminal -- python3 -m pytest