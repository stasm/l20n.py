TEST_FILES   := $(wildcard test_*.py)
TEST_MODULES := $(TEST_FILES:%.py=%)

test:
	 PYTHONPATH=../.. python -m unittest $(TEST_MODULES)
