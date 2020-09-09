import unittest
from utils.utils import price_formatted


class UtilsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.val = 10000.00

    def test_price_formatted_return_string(self):
        self.assertEqual(price_formatted(self.val), f'R$ 10000,00')


if __name__ == '__main__':
    unittest.main()
