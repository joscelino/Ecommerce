from django.test import TestCase
from model_mommy import mommy

from apps.costumer.models import Costumer, CostumerAddress


class CostumerTestCase(TestCase):

    def setUp(self):
        self.user = mommy('user')

    def test_str(self):
        self.assertEquals(str(self.user), self.user.user)






