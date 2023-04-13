# test_loancalc.py

# assert expression
## if true nothing happens
## if false raises AssertionError

# create virtual environment and activate
# pip install pytest
# pip install pytest-cov

# run tests with python -m pytest -s
# compare -s and -v when running the tests
# run coverage tests with python -m pytest --cov

import pytest
from oop_loan_pmt import *

loanAmount = 100000
numberYears = 30
annualRate = 0.06
expectedMonthlyPayment = 599.55

### Unit Tests ###
def test_calculateDiscountFactor():
    loan = Loan(loanAmount, numberYears, annualRate)
    loan.calculateDiscountFactor()
    assert loan.getDiscountFactor() == pytest.approx(166.7916, rel=1e-4)

def test_calculateLoanPmt():
    loan = Loan(loanAmount, numberYears, annualRate)
    loan.calculateLoanPmt()
    assert loan.getLoanPmt() == pytest.approx(expectedMonthlyPayment, rel=1e-2)

### Functional Tests ###
def test_collectLoanDetails():
    loan = collectLoanDetails()
    assert loan.loanAmount == loanAmount
    assert loan.numberOfPmts == numberYears * 12
    assert loan.annualRate == annualRate

