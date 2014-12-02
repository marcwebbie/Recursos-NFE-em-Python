import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nfe import NotaFiscalEletronica

class NotaFiscalEletronicaTests(unittest.TestCase):
    def test_nfe_instantiation(self):
        nota_fiscal_eletronica = NotaFiscalEletronica()
        self.assertIsNotNone(nota_fiscal_eletronica)

if __name__ == "__main__":
    unittest.main()
