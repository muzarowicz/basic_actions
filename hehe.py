import pytest

@pytest.fixture()
def my_fixture(request):
    data = {'x': 1, 'y': 2, 'z': 3}

    def fin():
        print "\nMic drop"
    request.addfinalizer(fin)

    return data
