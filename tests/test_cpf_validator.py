import unittest
from utils.cpfvalidator import cpf_validator


class CpfValidatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.cpf_false = str(11111111111)
        self.cpf_true = str(26363277035)
        self.cpf_len = len(self.cpf_true)
        self.cpf_none = ''
        self.cpf_false = False
        self.cpf_invalid = str('234hd539hdj845')

    def test_cpf_validator(self):
        self.assertFalse(cpf_validator(self.cpf_false))
        self.assertTrue(cpf_validator(self.cpf_true))
        self.assertEqual(self.cpf_len, 11)
        self.assertFalse(cpf_validator(self.cpf_none))
        self.assertFalse(cpf_validator(self.cpf_false))
        self.assertFalse(cpf_validator(self.cpf_invalid))
        self.assertRegex(self.cpf_true, '26363277035')
        self.assertNotEqual(cpf_validator(self.cpf_false), cpf_validator(self.cpf_true))


if __name__ == '__main__':
    unittest.main()