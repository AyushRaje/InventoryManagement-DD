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
        if not cart.appliedDiscount:
            cart.discountedPrice = cart.cartValue
        self.inventory[productId].quantity -= quantity
        return {"message": f"Added {quantity} of {self.inventory[productId].name} to cart for customer {customerId}."}

    def apply_discount_coupon(self, customerId, discountId):
        if discountId not in self.discountCoupons:
            return {"error": "Invalid discount coupon."}
        cart = self.carts[customerId]

        if discountId in cart.appliedDiscounts:
            return {"error": "This coupon is already applied on this cart."}
        cart.appliedDiscounts[discountId] = discountId
        discountCoupon = self.discountCoupons[discountId]
        discountedPrice = (cart.cartValue * discountCoupon.discountPercentage)/100
        
        if discountedPrice > cart.cartValue:
            discountedPrice = 0
        
        elif discountedPrice > discountCoupon.maxDiscountCap :
            discountedPrice = cart.cartValue - discountCoupon.maxDiscountCap
        
        else:
            discountedPrice = cart.cartValue - discountedPrice

        cart.discountedPrice = discountedPrice    

        return {"message": f"Discount {discountId} applied to the cart."}

    def add_discount_coupon(self, discountId, discountPercentage, maxDiscountCap):
        self.discountCoupons[discountId] = DiscountCoupon(discountId, discountPercentage, maxDiscountCap)
        return {"message": f"Added discount coupon with ID {discountId}."}