from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
    
        Menu.objects.create(ID=1, Title="Pizza", Price=120, Inventory=50)
        Menu.objects.create(ID=2, Title="Burger", Price=50, Inventory=100)
        self.client = APIClient()

    def test_getall(self):
        
        response = self.client.get('/restaurant/menu/') 
        
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
        self.assertEqual(response.data, serializer.data)