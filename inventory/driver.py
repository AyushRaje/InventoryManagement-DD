from models import InventoryManagementSystem

if __name__ == '__main__':
    ims = InventoryManagementSystem()

    # Add Product to inventory
    result = ims.add_item_to_inventory(productId="p1",name="laptop",quantity=10,price=1000)
    print(result)
    result = ims.add_item_to_inventory(productId="p2",name="phone",quantity=5,price=500)
    print(result)

    # View Inventory
    inventory_data = {product.productId: {"name": product.name, "quantity": product.quantity,"price":product.price} for product in ims.inventory.values()}
    discounts = {discount.discountId: {"discount_percentage": discount.discountPercentage,"max_cap":discount.maxDiscountCap} for discount in ims.discountCoupons.values()}
    print("Inventory: ")
    print(inventory_data)
    print(discounts)

    # Remove item from Inventory
    result = ims.remove_item_from_inventory(productId="p1",quantity=3)
    print(result)

    # Add item to cart
    result = ims.add_item_to_cart(customerId="c1",productId="p1",quantity=4)
    print(result)
    
    # Remove item from cart
    result = ims.remove_from_cart(customerId="c1",productId="p1",quantity=2)
    print(result)

    # Add Discount coupon to Inventory
    result = ims.add_discount_coupon(discountId="d1",discountPercentage=20,maxDiscountCap=200)
    print(result)

    # Apply Discount to cart
    result = ims.apply_discount_coupon(customerId="c1",discountId="d1")
    print(result)

    # View cart
    result = ims.view_cart(customerId="c1")
    print(result)

    # Remove Discount from cart
    result = ims.remove_discount_from_cart(customerId="c1")
    print(result)




