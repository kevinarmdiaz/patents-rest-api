from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


API_PATENT_URL = reverse('get-patent')
class PatentsTestCase(APITestCase):

    def test_get_id_by_patent(self):
        """Test that get id by patent"""
        patent = 'AAAA003'
        response = self.client.get(API_PATENT_URL, {'patent': patent})
        self.assertEqual(response.data, {f'Id of Patent {patent} is': 4})
    
    def test_get_patent_by_id(self):
        """Test that patent by id"""
        id = '10'
        response = self.client.get(API_PATENT_URL, {'id': id})
        self.assertEqual(response.data, {f"Patent of Id {id} is": 'AAAA009'})
        id = '1001'
        response = self.client.get(API_PATENT_URL, {'id': id})
        self.assertEqual(response.data, {f"Patent of Id {id} is": 'BBBB000'})

        


