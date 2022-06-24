import unittest
from income_tax_calculator import IncomeTaxCalculator
from tax_payer import TaxPayer
from test.TestUtils import TestUtils

class FuctionalTests(unittest.TestCase):
    def test_add_tax_payer(self):
        tp=TaxPayer("Venu","AOOPT0045K",30,"venu@iiht.com",600000.00,24000,2400)
        IncomeTaxCalculator.add_tax_payer(tp)
        test_obj = TestUtils()
        if len(IncomeTaxCalculator.tax_payer_list)!=0:
            test_obj.yakshaAssert("TestAddTaxPayer", True, "functional")
            print("TestAddTaxPayer = Passed")
        else:
            test_obj.yakshaAssert("TestAddTaxPayer", False, "functional")
            print("TestAddTaxPayer = Failed")

    def test_return_typeof_total_deductions(self):
        total_deduct=IncomeTaxCalculator.total_deductions("AOOPT0045K")
        test_obj = TestUtils()
        if type(total_deduct)==type(1.0):
            test_obj.yakshaAssert("TestReturnTypeofTotalDeductions", True, "functional")
            print("TestReturnTypeofTotalDeductions = Passed")
        else:
            test_obj.yakshaAssert("TestReturnTypeofTotalDeductions", False, "functional")
            print("TestReturnTypeofTotalDeductions = Failed")

    def test_total_deductions(self):
        total_deduct=IncomeTaxCalculator.total_deductions("AOOPT0045K")
        test_obj = TestUtils()
        if total_deduct!=None:
            test_obj.yakshaAssert("TestTotalDeductions", True, "functional")
            print("TestTotalDeductions = Passed")
        else:
            test_obj.yakshaAssert("TestTotalDeductions", False, "functional")
            print("TestTotalDeductions = Failed")

    def test_deduction_list(self):
        total_deduct=IncomeTaxCalculator.total_deductions("AOOPT0045K")
        test_obj = TestUtils()
        if len(IncomeTaxCalculator.deduction_list)!=0:
            test_obj.yakshaAssert("TestDeductionList", True, "functional")
            print("TestDeductionList = Passed")
        else:
            test_obj.yakshaAssert("TestDeductionList", False, "functional")
            print("TestDeductionList = Failed")

    def test_tax_details_list(self):
        total_deduct=IncomeTaxCalculator.cal_tax("AOOPT0045K")
        test_obj = TestUtils()
        if len(IncomeTaxCalculator.tax_details_list)!=0:
            test_obj.yakshaAssert("TestTaxDetailsList", True, "functional")
            print("TestTaxDetailsList = Passed")
        else:
            test_obj.yakshaAssert("TestTaxDetailsList", False, "functional")
            print("TestTaxDetailsList = Failed")

    def test_show_taxable_salary(self):
        self.tp=TaxPayer("Chary","BOOPT0045L",40,"chary@iiht.com",600000.00,24000,2400)
        IncomeTaxCalculator.add_tax_payer(self.tp)
        IncomeTaxCalculator.total_deductions("BOOPT0045L")
        IncomeTaxCalculator.cal_tax("BOOPT0045L")
        taxable_salary=IncomeTaxCalculator.show_taxable_salary("BOOPT0045L")
        test_obj = TestUtils()
        if taxable_salary!=None:
            test_obj.yakshaAssert("TestShowTaxableSalary", True, "functional")
            print("TestShowTaxableSalary = Passed")
        else:
            test_obj.yakshaAssert("TestShowTaxableSalary", False, "functional")
            print("TestShowTaxableSalary = Failed")

    def test_show_total_tax(self):
        total_tax=IncomeTaxCalculator.show_total_tax("BOOPT0045L")
        test_obj = TestUtils()
        if total_tax!=None:
            test_obj.yakshaAssert("TestShowTotalTax", True, "functional")
            print("TestShowTotalTax = Passed")
        else:
            test_obj.yakshaAssert("TestShowTotalTax", False, "functional")
            print("TestShowTotalTax = Failed")
