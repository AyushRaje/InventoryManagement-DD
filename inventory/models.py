class Product:
    def __init__(self, productId, name, quantity,price):
        self.productId = productId
        self.name = name
        self.quantity = quantity
        self.price = price

class Cart:
    def __init__(self, customerId):
        self.customerId = customerId
        self.products = {}
        self.cartValue = 0
        self.discountedPrice = self.cartValue
        self.appliedDiscounts = {}

class DiscountCoupon:
    def __init__(self, discountId, discountPercentage, maxDiscountCap):
        self.discountId = discountId
        self.discountPercentage = discountPercentage
        self.maxDiscountCap = maxDiscountCap

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}
        self.carts = {}
        self.discountCoupons = {}

    def add_item_to_inventory(self, productId, name, quantity,price):
        if productId in self.inventory:
            self.inventory[productId].quantity += quantity
            if name != self.inventory[productId].name:
                message = f"""Added {quantity} of {name} to inventory.\n 
                Changed product name from  {self.inventory[productId].name} to {name}"""
                self.inventory[productId].name = name
                return {"message":message }
        else:
            self.inventory[productId] = Product(productId, name, quantity,price)
        return {"message": f"Added {quantity} of {name} to inventory."}

    def remove_item_from_inventory(self, productId, quantity):
        if productId in self.inventory:
            if self.inventory[productId].quantity >= quantity:
                self.inventory[productId].quantity -= quantity
                if self.inventory[productId].quantity == 0:
                    del self.inventory[productId]
                return {"message": f"Removed {quantity} of {self.inventory[productId].name} from inventory."}
            else:
                return {"error": "Not enough quantity to remove."}
        else:
            return {"error": "Product not found in inventory."}
    
    def remove_discount_from_cart(self,customerId):
        if customerId not in self.carts:
            return {"error": "Cart for this customer does not exists."}

        cart = self.carts[customerId]
        cart.discountedPrice = cart.cartValue
        cart.appliedDiscounts = {}

        return {"message": "Discount removed from the cart."}

    def evalute_cart_value(self,cart):
        cart_value = 0
        for productId in cart.products:
            cart_value += (self.inventory[productId].price * cart.products[productId])
        return cart_value    

    def add_item_to_cart(self, customerId, productId, quantity):
        if productId not in self.inventory: 
            return {"error": "Product does not exist in inventory."}

        if self.inventory[productId].quantity < quantity:
           return {"error": "Quantity requested is not available in inventory"} 

        if customerId not in self.carts:
            self.carts[customerId] = Cart(customerId)

        cart = self.carts[customerId]
        if productId in cart.products:
            cart.products[productId] += quantity
        else:
            cart.products[productId] = quantity

        cart.cartValue = self.evalute_cart_value(cart)
        if not cart.appliedDiscounts:
            cart.discountedPrice = cart.cartValue
        else:
            cart.discountPrice = self.calculate_discount_price(cart,cart.appliedDiscounts)    
        self.inventory[productId].quantity -= quantity
        return {"message": f"Added {quantity} of {self.inventory[productId].name} to cart for customer {customerId}."}

    def calculate_discount_price(self,cart,discountCoupon):
        if discountCoupon:
            discountedPrice = (cart.cartValue * discountCoupon['discountPercentage'])/100
            
            if discountedPrice > cart.cartValue:
                discountedPrice = 0
            
            elif discountedPrice > discountCoupon['maxDiscountCap'] :
                discountedPrice = cart.cartValue - discountCoupon['maxDiscountCap']
            
            else:
                discountedPrice = cart.cartValue - discountedPrice
        else:
            discountedPrice = cart.cartValue        

        return discountedPrice    

    def apply_discount_coupon(self, customerId, discountId):
        if discountId not in self.discountCoupons:
            return {"error": "Invalid discount coupon."}
        cart = self.carts[customerId]

        if cart.appliedDiscounts and discountId in cart.appliedDiscounts:
            return {"error": "This coupon is already applied on this cart."}

        discountCoupon = self.discountCoupons[discountId]
        cart.appliedDiscounts = discountCoupon.__dict__
        cart.discountedPrice = self.calculate_discount_price(cart,cart.appliedDiscounts)    

        return {"message": f"Discount {discountId} applied to the cart."}

    def add_discount_coupon(self, discountId, discountPercentage, maxDiscountCap):
        self.discountCoupons[discountId] = DiscountCoupon(discountId, discountPercentage, maxDiscountCap)
        return {"message": f"Added discount coupon with Id {discountId}."}
    
    def remove_from_cart(self,customerId,productId,quantity):
        if customerId not in self.carts:
            return {"error": f"Cart for this customer does not exists."}
        if not productId in self.carts[customerId].products:
            return {"error": f"Product does not exists in cart."}
        if quantity > self.carts[customerId].products[productId]:
            return {"error": f"Quantity of product to remove is greater than quantity in cart."}
        
        if quantity == self.carts[customerId].products[productId]:
            del self.carts[customerId].products[productId]
        else:
            self.carts[customerId].products[productId]-=quantity

        self.carts[customerId].cartValue = self.evalute_cart_value(self.carts[customerId])
        self.carts[customerId].discountedPrice = self.calculate_discount_price(self.carts[customerId],self.carts[customerId].appliedDiscounts)
        return {"message": f"Removed {quantity} of {productId} from the cart"}
    
    def view_cart(self,customerId):
        if customerId in self.carts:
            cart_data = {product_id: quantity for product_id, quantity in self.carts[customerId].products.items()}
            return {"customerId": customerId, "cart": cart_data,"cart_value":self.carts[customerId].cartValue,"discounted_value":self.carts[customerId].discountedPrice}
        else:
            return {"error": "Customer does not have a cart."}