""""
API Services
"""
from django.test import SimpleTestCase
from core.service.core_service import CoreService


class testServices(SimpleTestCase):

    def setUp(self) -> CoreService:
        self.core_service_instance = CoreService()
        return 

    # def test_init_db(self):
    #     current_db: str = 'stock-market-api'
    #     result: list = self.core_service_instance.init_db()

    #     self.assertIn(current_db, result)

    def test_display_value(self):
        
        result: int = self.core_service_instance.display_value(5,6)
        self.assertEqual(result , 11)