# Django E-Commerce Marketplace

A Django-based E-Commerce Marketplace that allows sellers to manage products and buyers to browse products, add items to a cart, and place orders online.

## Features

### Seller Features

* Seller Dashboard
* Add Products
* Edit Products
* Delete Products
* Upload Product Images
* View Seller Orders

### Buyer Features

* Browse Products
* View Product Details
* Add to Cart
* Remove from Cart
* Checkout System
* Order Placement

### Admin Features

* Manage Products
* Manage Orders
* Manage Users
* Django Admin Interface

## Technologies Used

* Python
* Django
* HTML
* CSS
* Bootstrap
* SQLite
* Git
* GitHub

## Project Structure

```text
ecommerce-site/
│
├── ecommerce/
├── products/
├── media/
├── manage.py
├── db.sqlite3
└── .gitignore
```

## Installation

### Clone Repository

```bash
git clone https://github.com/jathishkrishna/ecommerce-marketplace.git
cd ecommerce-marketplace
```

### Install Dependencies

```bash
pip install django pillow
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

## Screenshots

* Product Listing Page
* Product Detail Page
* Shopping Cart
* Checkout Page
* Seller Dashboard
* Django Admin Panel

## Future Enhancements

* Online Payment Gateway
* User Authentication
* Product Categories
* Search and Filters
* Wishlist
* Order Tracking
* Reviews and Ratings

## Author

**Jathish Krishna**

GitHub:
https://github.com/jathishkrishna

## License

This project is developed for educational and learning purposes.
