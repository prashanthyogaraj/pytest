import pytest


@pytest.fixture
def input_func():
    var=21
    return var
	
	
def pytest_collection_modifyitems(items):
    print(*items,sep="\n")
    for item in items:
        print(item.nodeid)
        item.add_marker(pytest.mark.light)