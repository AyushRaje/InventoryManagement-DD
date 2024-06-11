from django.apps import AppConfig
from inventory.models import InventoryManagementSystem

class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'
    global ims
    ims = InventoryManagementSystem()
