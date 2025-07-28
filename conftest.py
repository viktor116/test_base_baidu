import allure
from pytest import Item

def pytest_runtest_call(item: Item):
	if item.parent._obj.__doc__:
		allure.dynamic.feature(item.parent._obj.__doc__)

	if item.function.__doc__:
		allure.dynamic.title(item.function.__doc__)