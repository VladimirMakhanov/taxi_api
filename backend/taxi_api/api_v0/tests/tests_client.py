from django.test import TestCase
from rest_framework.test import APITestCase
from unittest import mock
from api_v0.models import Client


class ClientTestsBasic(TestCase):

    def setUp(self):
        super(ClientTestsBasic, self).setUp()

    # Representation tests
    def test_client_str_right(self):
        mock_instance = mock.Mock(spec=Client)
        mock_instance.name = 'Matt'
        self.assertEqual(Client.__str__(mock_instance), 'Matt')

    def test_client_str_wrong(self):
        mock_instance = mock.Mock(spec=Client)
        mock_instance.name = 'Matt'
        self.assertNotEqual(Client.__str__(mock_instance), 'Matt2')


class ClientTests(APITestCase):
    # CRUD tests
    # @mock.patch('api_v0.ClientSerializer')
    def test_create_client(self):
        url = reversed('clients')
        data = {'name': 'Matt Correct', 'phone': '+000 (00) 000 00 00'}
        mock_instance = mock.Mock(spec=Client)
        response = self.client.post()
        self.assertTrue(mock_instance.is_valid())

