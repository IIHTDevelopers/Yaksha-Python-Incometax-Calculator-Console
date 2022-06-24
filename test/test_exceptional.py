import unittest
from exception import *
from income_tax_calculator import IncomeTaxCalculator
from tax_payer import TaxPayer
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tp=TaxPayer("Venu","DOOPT0045K",30,"venu@iiht.com",600000.00,24000,2400)
        IncomeTaxCalculator.add_tax_payer(tp)
    def test_error_at_add_taxpayer(self):
        test_obj = TestUtils()
        try:
            tp=TaxPayer("Venu","DOOPT0045K",30,"venu@iiht.com",600000.00,24000,2400)
            IncomeTaxCalculator.add_tax_payer(tp)
            test_obj.yakshaAssert("TestErrorAtAddTaxpayer", False, "exception")
            print("TestErrorAtAddTaxpayer = Failed")
        except PANAlreadyExistsError:
            test_obj.yakshaAssert("TestErrorAtAddTaxpayer", True, "exception")
            print("TestErrorAtAddTaxpayer = Passed")
    def test_error_at_total_deductions(self):
        test_obj = TestUtils()
        try:
            IncomeTaxCalculator.total_deductions("COOPT0045R")
            test_obj.yakshaAssert("TestErrorAtTotalDeductions", False, "exception")
            print("TestErrorAtTotalDeductions = Failed")
        except PANDoesNotExistsError:
            test_obj.yakshaAssert("TestErrorAtTotalDeductions", True, "exception")
            print("TestErrorAtTotalDeductions = Passed")

    def test_error_at_cal_tax(self):
        test_obj = TestUtils()
        try:
            IncomeTaxCalculator.cal_tax("COOPT0045R")
            test_obj.yakshaAssert("TestErrorAtCalTax", False, "exception")
            print("TestErrorAtCalTax = Failed")
        except PANDoesNotExistsError:
            test_obj.yakshaAssert("TestErrorAtCalTax", True, "exception")
            print("TestErrorAtCalTax = Passed")

    def test_error_at_show_taxable_salary(self):
        test_obj = TestUtils()
        try:
            IncomeTaxCalculator.show_taxable_salary("COOPT0045R")
            test_obj.yakshaAssert("TestErrorAtShowTaxableSalary", False, "exception")
            print("TestErrorAtShowTaxableSalary = Failed")
        except PANDoesNotExistsError:
            test_obj.yakshaAssert("TestErrorAtShowTaxableSalary", True, "exception")
            print("TestErrorAtShowTaxableSalary = Passed")

    def test_error_at_show_total_tax(self):
        test_obj = TestUtils()
        try:
            IncomeTaxCalculator.show_total_tax("COOPT0045R")
            test_obj.yakshaAssert("TestErrorAtShowTotalTax", False, "exception")
            print("TestErrorAtShowTotalTax = Failed")
        except PANDoesNotExistsError:
            test_obj.yakshaAssert("TestErrorAtShowTotalTax", True, "exception")
            print("TestErrorAtShowTotalTax = Passed")
