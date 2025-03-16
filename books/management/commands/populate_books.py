from django.core.management.base import BaseCommand
from books.models import Book
from faker import Faker
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populates the database with sample books and performs CRUD operations'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Добавление 20 книг
        for _ in range(20):
            Book.objects.create(
                title=fake.sentence(nb_words=4),
                author=fake.name(),
                price=round(Decimal(random.uniform(10, 100)), 2),
                published_date=fake.date_between(start_date='-10y', end_date='today')
            )
        self.stdout.write(self.style.SUCCESS('Successfully added 20 books'))

        # Пример CRUD операций
        books = Book.objects.all()

        # Обновление первых 10 книг
        for book in books[:10]:
            book.price = round(book.price * Decimal('1.1'), 2)
            book.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated 10 books'))

        # Удаление последних 5 книг
        # Используем order_by и reverse для получения последних 5 записей
        last_books = Book.objects.order_by('-id')[:5]
        for book in last_books:
            book.delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted 5 books'))

        # Чтение оставшихся книг
        remaining_books = Book.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Remaining books in database: {remaining_books}'))
