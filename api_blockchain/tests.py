from django.test import TestCase
from django.test import Client


class TransferNormalTest(TestCase):

    def test_city_not_exist(self):
        data = {"src_account": "12345678901234567890123456",
                "des_account": "12345678901234567890123457",
                "amount": "12.32"}

        c = Client()
        response = c.post('/transfer_normal/', data)
        result = response.json()
        self.assertEqual(result.get('src_account'), data.get('src_account'))




