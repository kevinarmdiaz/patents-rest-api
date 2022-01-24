from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


API_PATENT_URL = reverse('get-patent')
class PatentsTestCase(APITestCase):

    def test_get_id_by_patent(self):
        """Test that get id by patent"""
        patent = 'AAAA003'
        data = {'patent': patent}
        response = self.client.get(API_PATENT_URL, data)
        self.assertEqual(response.data, {f'Id of Patent {patent} is': 4})
    
    def test_get_patent_by_id(self):
        """Test that patent by id"""
        id = '10'
        data = {'id': id}
        response = self.client.get(API_PATENT_URL, data)
        self.assertEqual(response.data, {f"Patent of Id {id} is": 'AAAA009'})

        


