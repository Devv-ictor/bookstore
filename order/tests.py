import pytest
from django.test import TestCase
from django.contrib.auth.models import User
from order.models import Order
from product.models import Product, Category


class OrderModelTest(TestCase):
    """Test cases for Order model."""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(
            title="Fiction",
            slug="fiction",
            description="Fiction books"
        )
        self.product = Product.objects.create(
            title="Test Book",
            description="A test book",
            price=2999,
            active=True
        )
        self.product.category.add(self.category)

    def test_order_creation(self):
        """Test that an order can be created."""
        order = Order.objects.create(user=self.user)
        order.products.add(self.product)

        self.assertEqual(order.user, self.user)
        self.assertEqual(order.products.count(), 1)
        self.assertIn(self.product, order.products.all())