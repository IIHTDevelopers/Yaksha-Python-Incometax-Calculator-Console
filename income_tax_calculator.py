from exception import PANDoesNotExistsError,PANAlreadyExistsError
from tax_details import TaxDetails
from tax_payer import TaxPayer
from deduction import Deductions
class IncomeTaxCalculator:
    pan_list=[]
    tax_payer_list=[]
    deduction_list=[]
    tax_details_list=[]

    @staticmethod
    def add_tax_payer(taxPayerObj):
        pass

    @staticmethod
    def total_deductions(PAN):
        pass

    @staticmethod
    def cal_tax(PAN):
        pass

    @staticmethod
    def show_taxable_salary(PAN):
        pass

    @staticmethod
    def show_total_tax(PAN):
        pass
