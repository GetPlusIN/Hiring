from django.test import TestCase
from .models import Book
from datetime import date
from django.urls import reverse




class BookTestCase(TestCase):
    
    def setUp(self):
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            description='This is a test book.',
            published_date=date(2020, 1, 1),
        )
    
    def test_book_title(self):
        self.assertEqual(str(self.book), 'Test Book')
        
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')
        
    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

