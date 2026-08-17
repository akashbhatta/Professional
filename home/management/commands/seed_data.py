import random
from datetime import timedelta
from decimal import Decimal

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from customer.models import Customer
from order.models import Order
from product.models import Category, Product
from suppliers.models import Supplier
from user.models import Role, User


CATEGORY_NAMES = [
    "Electronics",
    "Groceries",
    "Furniture",
    "Apparel",
    "Stationery",
    "Toys",
    "Beauty",
    "Automotive",
    "Sports",
    "Books",
    "Home Appliances",
    "Garden",
    "Pet Supplies",
    "Health",
    "Music",
]
ROLE_NAMES = ["Admin", "Manager", "Staff"]
FIRST_NAMES = [
    "Aarav",
    "Maya",
    "Nisha",
    "Rohan",
    "Sita",
    "Kabir",
    "Anika",
    "Dev",
    "Priya",
    "Samir",
]
LAST_NAMES = [
    "Sharma",
    "Karki",
    "Rai",
    "Thapa",
    "Gurung",
    "Maharjan",
    "Adhikari",
    "Basnet",
]
PRODUCT_WORDS = [
    "Wireless Mouse",
    "Desk Lamp",
    "Notebook Pack",
    "Storage Box",
    "Running Shoes",
    "Bluetooth Speaker",
    "Coffee Maker",
    "Garden Tool Set",
    "Backpack",
    "Water Bottle",
]
COMPANY_WORDS = [
    "Everest Traders",
    "Himal Supply",
    "Metro Wholesale",
    "Summit Goods",
    "Valley Imports",
    "Prime Distributors",
]


class Command(BaseCommand):
    help = "Seed the database with sample data for roles, users, categories, products, suppliers, customers, and orders."

    def add_arguments(self, parser):
        parser.add_argument("--users", type=int, default=10)
        parser.add_argument("--categories", type=int, default=10)
        parser.add_argument("--products", type=int, default=20)
        parser.add_argument("--suppliers", type=int, default=8)
        parser.add_argument("--customers", type=int, default=15)
        parser.add_argument("--orders", type=int, default=10)
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete existing rows before seeding.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        random.seed(42)

        if options["flush"]:
            Order.objects.all().delete()
            Product.objects.all().delete()
            Category.objects.all().delete()
            User.objects.all().delete()
            Role.objects.all().delete()
            Supplier.objects.all().delete()
            Customer.objects.all().delete()
            self.stdout.write(self.style.WARNING("Cleared existing seeded data."))

        roles = [Role.objects.get_or_create(name=name)[0] for name in ROLE_NAMES]

        users = self._seed_users(options["users"], roles)
        categories = self._seed_categories(options["categories"])
        products = self._seed_products(options["products"], categories)
        suppliers = self._seed_suppliers(options["suppliers"])
        customers = self._seed_customers(options["customers"])
        orders = self._seed_orders(options["orders"], customers, products)

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {len(users)} users, {len(categories)} categories, "
                f"{len(products)} products, {len(suppliers)} suppliers, "
                f"{len(customers)} customers, {len(orders)} orders."
            )
        )

    def _person_name(self, index):
        first = FIRST_NAMES[index % len(FIRST_NAMES)]
        last = LAST_NAMES[index % len(LAST_NAMES)]
        return f"{first} {last}"

    def _address(self, index):
        return f"House {index + 1}, Kathmandu"

    def _seed_users(self, count, roles):
        created = []
        for index in range(count):
            user, is_new = User.objects.get_or_create(
                email=f"user{index + 1}@example.com",
                defaults={
                    "name": self._person_name(index),
                    "phone": f"980000{index + 1:04d}",
                    "password": make_password("password123"),
                    "address": self._address(index),
                    "role": random.choice(roles),
                },
            )
            if is_new:
                created.append(user)
        return created

    def _seed_categories(self, count):
        names = CATEGORY_NAMES[:count]
        while len(names) < count:
            names.append(f"Category {len(names) + 1}")

        created = []
        for name in names:
            category, _ = Category.objects.get_or_create(name=name)
            created.append(category)
        return created

    def _seed_products(self, count, categories):
        category_names = [category.name for category in categories] or CATEGORY_NAMES
        created = []
        for index in range(count):
            product_name = f"{PRODUCT_WORDS[index % len(PRODUCT_WORDS)]} {index + 1}"
            product, is_new = Product.objects.get_or_create(
                name=product_name,
                defaults={
                    "price": Decimal(f"{random.uniform(5, 999):.2f}"),
                    "quantity": random.randint(5, 200),
                    "category": random.choice(category_names),
                },
            )
            if is_new:
                created.append(product)
        return created

    def _seed_suppliers(self, count):
        created = []
        for index in range(count):
            supplier, is_new = Supplier.objects.get_or_create(
                email=f"supplier{index + 1}@example.com",
                defaults={
                    "name": f"{COMPANY_WORDS[index % len(COMPANY_WORDS)]} {index + 1}",
                    "phone": f"970000{index + 1:04d}",
                    "address": self._address(index),
                    "is_active": True,
                },
            )
            if is_new:
                created.append(supplier)
        return created

    def _seed_customers(self, count):
        created = []
        for index in range(count):
            customer, is_new = Customer.objects.get_or_create(
                email=f"customer{index + 1}@example.com",
                defaults={
                    "name": self._person_name(index + 3),
                    "phone": f"981000{index + 1:04d}",
                    "password": make_password("password123"),
                    "address": self._address(index + 20),
                },
            )
            if is_new:
                created.append(customer)
        return created

    def _seed_orders(self, count, customers, products):
        customers = customers or list(Customer.objects.all())
        products = products or list(Product.objects.all())
        if not customers or not products:
            self.stdout.write(
                self.style.WARNING(
                    "Skipping orders: need at least one customer and one product."
                )
            )
            return []

        statuses = [choice[0] for choice in Order.OrderStatus.choices]
        created = []
        today = timezone.localdate()
        for index in range(count):
            order = Order.objects.create(
                customer=random.choice(customers),
                order_date=today - timedelta(days=random.randint(0, 90)),
                status=random.choice(statuses),
            )
            order.order_details.set(
                random.sample(products, k=min(len(products), random.randint(1, 4)))
            )
            created.append(order)
        return created
