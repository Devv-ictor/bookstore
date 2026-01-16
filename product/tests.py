import pytest
from django.test import TestCase
from product.models import Product, Category


class CategoryModelTest(TestCase):
    """Test cases for Category model."""

    def test_category_creation(self):
        """Test that a category can be created."""
        category = Category.objects.create(
            title="Fiction",
            slug="fiction",
            description="Fiction books",
            active=True
        )
        self.assertEqual(category.title, "Fiction")
        self.assertEqual(category.slug, "fiction")
        self.assertTrue(category.active)


class ProductModelTest(TestCase):
    """Test cases for Product model."""

    def setUp(self):
        self.category = Category.objects.create(
            title="Fiction",
            slug="fiction",
            description="Fiction books"
        )

    def test_product_creation(self):
        """Test that a product can be created."""
        product = Product.objects.create(
            title="Test Book",
            description="A test book description",
            price=2999,
            active=True
        )
        product.category.add(self.category)

        self.assertEqual(product.title, "Test Book")
        self.assertEqual(product.price, 2999)
        self.assertTrue(product.active)
        self.assertEqual(product.category.count(), 1)