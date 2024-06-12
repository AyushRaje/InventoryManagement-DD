from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from inventory.models import InventoryManagementSystem
import json
from inventory.apps import ims



@method_decorator(csrf_exempt, name='dispatch')
class AddItemToInventoryView(View):
    def post(self, request):
        status = True
        try:
            data = json.loads(request.body)
            productId = data.get('productId')
            name = data.get('name')
            quantity = data.get('quantity')
            price = data.get('price')
            result = ims.add_item_to_inventory(productId, name, quantity,price)
        except Exception as e:
            return JsonResponse({"error":str(e)})    
        
        return JsonResponse(result)

@method_decorator(csrf_exempt, name='dispatch')
class RemoveItemFromInventoryView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            productId = data.get('productId')
            quantity = data.get('quantity')
            result = ims.remove_item_from_inventory(productId, quantity)

        except Exception as e:
            return JsonResponse({"error":str(e)})  
          
        return JsonResponse(result)

@method_decorator(csrf_exempt, name='dispatch')
class AddItemToCartView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            customerId = data.get('customerId')
            productId = data.get('productId')
            quantity = data.get('quantity')
            result = ims.add_item_to_cart(customerId, productId, quantity)
        except Exception as e:
            return JsonResponse({"error":str(e)})  
          
        return JsonResponse(result)

@method_decorator(csrf_exempt, name='dispatch')
class ApplyDiscountCouponView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            discountId = data.get('discountId')
            customerId = data.get('customerId')
            result = ims.apply_discount_coupon(customerId, discountId)

        except Exception as e:
            return JsonResponse({"error":str(e)})    
        
        return JsonResponse(result)

@method_decorator(csrf_exempt, name='dispatch')
class AddDiscountCouponView(View):
    def post(self, request):
        try: 
            data = json.loads(request.body)
            discountId = data.get('discountId')
            discountPercentage = data.get('discountPercentage')
            maxDiscountCap = data.get('maxDiscountCap')
            result = ims.add_discount_coupon(discountId, discountPercentage, maxDiscountCap)
        except Exception as e:
            return JsonResponse({"error":str(e)})

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')    
class ViewInventoryView(View):
    def get(self, request):
        try:
            inventory_data = {product.productId: {"name": product.name, "quantity": product.quantity,"price":product.price} for product in ims.inventory.values()}
        except Exception as e:
            return JsonResponse({"error":str(e)})    
        
        return JsonResponse(inventory_data) 
    
@method_decorator(csrf_exempt, name='dispatch') 
class ViewCartView(View):
    def get(self, request):
        try:
            customer_id = request.GET.get('customerId', None)
            if customer_id:
                if customer_id in ims.carts:
                    cart_data = {product_id: quantity for product_id, quantity in ims.carts[customer_id].products.items()}
                    return JsonResponse({"customerId": customer_id, "cart": cart_data,"cart_value":ims.carts[customer_id].cartValue,"discounted_value":ims.carts[customer_id].discountedPrice})
                else:
                    return JsonResponse({"error": "Customer does not have a cart."})
            else:
                return JsonResponse({"error": "customerId parameter is required."})

        except Exception as e:
            return JsonResponse({"error":str(e)})        
          
@method_decorator(csrf_exempt, name='dispatch') 
class RemoveItemFromCartView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            customerId = data.get('customerId')
            productId = data.get('productId')
            quantity = data.get('quantity')
            result = ims.remove_from_cart(customerId,productId,quantity)
        except Exception as e:
            return JsonResponse({"error":str(e)})    
        
        return JsonResponse(result)

@method_decorator(csrf_exempt, name='dispatch') 
class RemoveDiscountFromCartView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            customerId = data.get('customerId')
            result = ims.remove_discount_from_cart(customerId)
        except Exception as e:
            return JsonResponse({"error":str(e)})

        return JsonResponse(result)

