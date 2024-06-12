# InventoryManagement-DD
This project is an implementation of an inventory management system for an e-commerce store using **Django**. The system allows administrators to manage product inventory and enables customers to add products to their cart and apply discount coupons. This implementation does not use any external databases or services; it uses in-memory data structures.
## Requirements
1. Python 3.8+
2. Django 4.9.0+

## Postman Collection for Testing:
The project is deployed in **Vercel** and the postman collection for the same is given below.
<br>
https://www.postman.com/altimetry-participant-28686498/workspace/public-projects/collection/28653510-0088f122-3830-4b0c-b935-8f3468dd5eb3?action=share&creator=28653510

## Setup
1. Clone the repository:
```
git clone <repository-url>
cd inventory_management
```
2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install dependencies and requirements
```
pip install -r requirements.txt
```
4. To start the server run:
```
python manage.py runserver
```

## Test
Run **driver.py** in **./inventory** to test all the functionalities 


## File structure and description

- **inventory/**: Contains the main application code for inventory management.
  - **\_\_pycache\_\_/**: Stores the bytecode cache of the Python files.
  - **migrations/**: Contains migration files for the Django ORM.
  - **\_\_init\_\_.py**: Initializes the `inventory` module.
  - **admin.py**: Registers models for the Django admin interface.
  - **apps.py**: Configures the app settings for `inventory`.
  - **driver.py**: Driver function to test functionalities.
  - **models.py**: Contains the Class definitions for the application.
  - **tests.py**: Contains test cases for the application.
  - **urls.py**: URL routing for the `inventory` app.
  - **views.py**: Contains the view functions for handling requests.

- **inventory_management/**: Contains the project-wide settings and configurations.
  - **\_\_pycache\_\_/**: Stores the bytecode cache of the Python files.
  - **\_\_init\_\_.py**: Initializes the `inventory_management` module.
  - **asgi.py**: ASGI configuration for asynchronous support.
  - **settings.py**: Project settings configuration.
  - **urls.py**: URL routing for the project.
  - **wsgi.py**: WSGI configuration for deploying the project.

- **venv/**: (Python Virtual Environment directory, contains installed dependencies)

- **.gitignore**: Specifies files and directories to be ignored by Git.

- **db.sqlite3**: SQLite database file(Not is use,created by default settings)

- **manage.py**: Command-line utility for managing the Django project.

- **README.md**: Project description and structure.

- **requirements.txt**: List of dependencies required for the project.

- **vercel.json**: Configuration file for deploying the project on Vercel.

## Implementation
### Data Structures
Since we are not using a database, we simulate the models using Python classes. These classes are defined in api/models.py. These classes are used to simulate the models and their relationships without relying on database. Below is a detailed explanation of each class:

### 1. Product

- Purpose: Represents a product in the inventory.
- Attributes:
    - productId: A unique identifier for the product.
    - name: The name of the product.
    - quantity: The available quantity of the product in the inventory.
    - price: price of 1 unit of product.
- Methods: None
### 2. Cart
  
- Purpose: Represents a customer's shopping cart.
- Attributes:
    - customerId: A unique identifier for the customer.
    - products: A dictionary that maps product IDs to their quantities in the cart.
    - cartValue: The total value of the cart.
    - discountedPrice: Price after applying a valid discount coupon.
    - appliedDiscounts: Details of coupon applied to the cart. 
- Methods: None.
### 3. DiscountCoupon

- Purpose: Represents a discount coupon that can be applied to a cart.
- Attributes:
    - discountId: A unique identifier for the discount coupon.
    - discountPercentage: The percentage discount the coupon provides.
    - maxDiscountCap: The maximum discount amount that can be applied.
- Methods: None.
### 4. InventoryManagementSystem
- Purpose: Manages the inventory, carts, and discount coupons. Provides methods to interact with these data structures.
- Attributes:
  - inventory: A dictionary that maps product IDs to Product instances.
  - carts: A dictionary that maps customer IDs to Cart instances.
  - discountCoupons: A dictionary that maps discount IDs to DiscountCoupon instances.
- Methods:

  - add_item_to_inventory(productId, name, quantity, price): Adds a product to the inventory.
  - remove_item_from_inventory(productId, quantity): Removes a specified quantity of a product from the inventory.
  - remove_discount_from_cart(customerId): Removes all applied discounts from the cart.
  - evalute_cart_value(cart): Calculates the total value of the items in the cart.
  - add_item_to_cart(customerId, productId, quantity): Adds a specified quantity of a product to a customer's cart.
  - calculate_discount_price(cart, discountCoupon): Calculates the discounted price of the cart after applying the discount coupon.
  - apply_discount_coupon(customerId, discountId): Applies a discount coupon to the cart value and returns the discounted price.
  - add_discount_coupon(discountId, discountPercentage, maxDiscountCap): Adds a discount coupon to the system.
  - remove_from_cart(customerId, productId, quantity): Removes a specified quantity of a product from a customer's cart.
  - view_cart(customerId): Returns the details of the customer's cart, including products, cart value, and discounted value.

## Testing the APIs
You can test the APIs using tools like Postman or curl. Below are some example requests:

### 1. Add item to inventory:
```
curl -X POST http://127.0.0.1:8000/api/add_item_to_inventory/ -H "Content-Type: application/json" -d '{
    "productId": "p1",
    "name": "Laptop",
    "quantity": 10,
    "price": 50000
}'

```
### 2. Remove item from inventory::
```
curl -X POST http://127.0.0.1:8000/api/remove_item_from_inventory/ -H "Content-Type: application/json" -d '{
    "productId": "p1",
    "quantity": 5
}'

```
### 3. Add Item to Cart:
```
curl -X POST http://127.0.0.1:8000/api/add_item_to_cart/ -H "Content-Type: application/json" -d '{
    "customerId": "c1",
    "productId": "p1",
    "quantity": 2
}'


```
### 4. Add Discount Coupon:
```
curl -X POST http://127.0.0.1:8000/api/add_discount_coupon/ -H "Content-Type: application/json" -d '{
    "discountId": "d1",
    "discountPercentage": 20,
    "maxDiscountCap": 150
}'

```
### 5. Add item to inventory:
```
curl -X POST http://127.0.0.1:8000/api/add_item_to_inventory/ -H "Content-Type: application/json" -d '{
    "productId": "p1",
    "name": "Laptop",
    "quantity": 10,
    "price": 50000
}'

```
### 6. Apply Discount Coupon:
```
curl -X POST http://127.0.0.1:8000/api/apply_discount_coupon/ -H "Content-Type: application/json" -d '{
    "customerId": "c1",
    "discountId": "d1"
}'

```
### 7. Remove Item from Cart:
```
curl -X POST http://127.0.0.1:8000/api/remove_from_cart/ -H "Content-Type: application/json" -d '{
    "customerId": "c1",
    "productId": "p1",
    "quantity": 1
}'

```
### 8. View Cart:
```
curl -X GET http://127.0.0.1:8000/api/view_cart/ -H "Content-Type: application/json" -d '{
    "customerId": "c1"
}'
```

### 9. Remove Discount from Cart:
```
curl -X POST http://127.0.0.1:8000/api/remove_discount_from_cart/ -H "Content-Type: application/json" -d '{
    "customerId": "c1"
}'

```
### 10. Remove Discount from Cart:
```
curl -X POST http://127.0.0.1:8000/api/reset_inventory/

```
### 11. View Inventory:
```
curl -X GET http://127.0.0.1:8000/api/view_inventory/

```


## Edge Cases Covered
### 1. Adding Items to Inventory:

- Adding a new product with an existing product ID updates the quantity and optionally the name.
- Adding a product with a zero or negative quantity is handled.
### 2. Removing Items from Inventory:

- Attempting to remove more items than available in the inventory returns an error.
- Removing items from a product that does not exist in the inventory returns an error.
### 3. Adding Items to Cart:

- Attempting to add a product that does not exist in the inventory returns an error.
- Attempting to add more items to the cart than available in the inventory returns an error.
### 4. Applying Discount Coupons:

- Applying a non-existent discount coupon returns an error.
- Applying a discount coupon that is already applied to the cart returns an error.
- The discounted price cannot be more than the cart value.
### 5. Removing Items from Cart:

- Attempting to remove more items from the cart than available returns an error.
- Removing a product that does not exist in the cart returns an error.
### 6. Removing Discount from Cart:

- Removing a discount from a cart that does not exist returns an error.
### 7. Viewing Cart:
- Viewing a cart that does not exist returns an error. 


