import pytest
from oop_loan_pmt import *

def test_calculate_loan_pmt():
    loan = Loan(100000, 30, 0.06)
    loan.calculateLoanPmt()
    assert round(loan.getLoanPmt(), 2) == 599.55

def test_get_discount_factor():
    loan = Loan(100000, 30, 0.06)
    loan.calculateDiscountFactor()
    assert round(loan.getDiscountFactor(), 4) == 166.7916
