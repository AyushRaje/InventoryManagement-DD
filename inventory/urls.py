from django.urls import path


from .views import (
    AddItemToInventoryView,
    RemoveItemFromInventoryView,
    AddItemToCartView,
    ApplyDiscountCouponView,
    AddDiscountCouponView,
    ViewInventoryView,
    ViewCartView,
    RemoveItemFromCartView,
    RemoveDiscountFromCartView
)

urlpatterns = [
    path('add_item_to_inventory/', AddItemToInventoryView.as_view(), name='add_item_to_inventory'),
    path('remove_item_from_inventory/', RemoveItemFromInventoryView.as_view(), name='remove_item_from_inventory'),
    path('add_item_to_cart/', AddItemToCartView.as_view(), name='add_item_to_cart'),
    path('apply_discount_coupon/', ApplyDiscountCouponView.as_view(), name='apply_discount_coupon'),
    path('add_discount_coupon/', AddDiscountCouponView.as_view(), name='add_discount_coupon'),
    path('view_inventory/', ViewInventoryView.as_view(), name='view_inventory'),
    path('view_cart/', ViewCartView.as_view(), name='view_cart'),
    path('remove_item_from_cart/',RemoveItemFromCartView.as_view(), name='remove_item_from_cart'),
    path('remove_discount_from_cart/',RemoveDiscountFromCartView.as_view(), name='remove_discount_from_cart'),
    
]