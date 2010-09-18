from django.test import TestCase

from utils.tools import capwords


class UtilsTestCase(TestCase):
    def testCapwords(self):
        input_one = 'hey you'
        self.assertEquals(capwords(input_one), 'Hey You')
        input_two = 'HEY YOU'
        self.assertEquals(capwords(input_two), 'Hey You')
         
