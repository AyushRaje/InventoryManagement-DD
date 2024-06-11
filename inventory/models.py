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
        self.cart_value = 0

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

    def add_item_to_inventory(self, productId, name, quantity):
        if productId in self.inventory:
            self.inventory[productId].quantity += quantity
        else:
            self.inventory[productId] = Product(productId, name, quantity)
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

    def add_item_to_cart(self, customerId, productId, quantity):
        if productId not in self.inventory or self.inventory[productId].quantity < quantity:
            return {"error": "Item not available in inventory."}

        if customerId not in self.carts:
            self.carts[customerId] = Cart(customerId)

        cart = self.carts[customerId]
        if productId in cart.products:
            cart.products[productId] += quantity
        else:
            cart.products[productId] = quantity

        self.inventory[productId].quantity -= quantity
        return {"message": f"Added {quantity} of {self.inventory[productId].name} to cart for customer {customerId}."}

    def apply_discount_coupon(self, cartValue, discountId):
        if discountId not in self.discountCoupons:
            return {"error": "Invalid discount coupon."}

        discountCoupon = self.discountCoupons[discountId]
        discountAmount = (discountCoupon.discountPercentage / 100) * cartValue
        discountAmount = min(discountAmount, discountCoupon.maxDiscountCap)
        discountedPrice = cartValue - discountAmount
        return {"discounted_price": discountedPrice, "message": f"Discount applied: {discountAmount}. Total price after discount: {discountedPrice}."}

    def add_discount_coupon(self, discountId, discountPercentage, maxDiscountCap):
        self.discountCoupons[discountId] = DiscountCoupon(discountId, discountPercentage, maxDiscountCap)
        return {"message": f"Added discount coupon with ID {discountId}."}