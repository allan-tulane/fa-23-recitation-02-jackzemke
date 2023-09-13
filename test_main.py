from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 40
	assert simple_work_calc(20, 3, 2) == 263.75
	assert simple_work_calc(30, 4, 2) == 930
	assert simple_work_calc(10, 5, 2) == 253.75
	assert simple_work_calc(20, 4, 2) == 620.0
	assert simple_work_calc(30, 3, 2) == 395.625

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 532.8125
	assert work_calc(30, 3, 2, lambda n: n) == 395.625
	assert work_calc(10, 5, 2,lambda n: 1) == 156
	assert work_calc(20, 4, 2, lambda n: n*n) == 2000
	assert work_calc(30, 2, 2, lambda n: n) == 150
