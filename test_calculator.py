'''
    This is unit test module for calculator.py module.
'''


import calculator


class TestCalculator:

    def test_add(self):
        assert 4 == calculator.addnumbers(2, 2)

    def test_subt(self):
        assert 2 == calculator.subtnumbers(4, 2)
