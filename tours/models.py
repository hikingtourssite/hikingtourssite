from django.db import models
from django.contrib.auth.models import User

# Represents a single hiking tour
class Tour(models.Model):
    title = models.CharField(max_length=200, verbose_name="Тур")  # Name of the tour
    description = models.TextField(verbose_name="Опис")  # Detailed description of the tour
    location = models.CharField(max_length=100, verbose_name="Локація")  # Where the tour takes place
    start_date = models.DateField(verbose_name="Початок")  # Start date of the tour
    end_date = models.DateField(verbose_name="Початок")  # End date of the tour
    guide_name = models.CharField(max_length=100, verbose_name="Гід")  # Name of the guide or organizer
    difficulty = models.CharField(max_length=50, verbose_name="Складність")  # Difficulty level (easy/medium/hard)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Вартість")  # Price per participant
    image = models.ImageField(upload_to='tours/', null=True, blank=True, verbose_name="Зображення")  # Optional tour image
    is_completed = models.BooleanField(default=False, verbose_name="Завершено")  # Whether the tour is completed
    is_cancelled = models.BooleanField(default=False, verbose_name="Відмінено")  # Whether the tour was cancelled

    def __str__(self):
        return self.title  # Display tour title in admin and elsewhere
    
    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Тури"

# Represents a booking for a tour made by a user
class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name="Тур")  # The tour that is being booked
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Користувач")  # New!
    full_name = models.CharField(max_length=100, verbose_name="Ім’я")  # Name of the person booking
    email = models.EmailField(verbose_name="Email")  # Contact email
    participants = models.PositiveIntegerField(verbose_name="Кількість учасників")  # Number of people booked
    confirmed = models.BooleanField(default=False, verbose_name="Підтверджено")  # Has the booking been confirmed?
    created_at = models.DateTimeField(auto_now_add=True)  # When the booking was made

    def __str__(self):
        return f'{self.full_name} → {self.tour.title}'  # Display format for booking
    
    class Meta:
        verbose_name = "Бронювання"
        verbose_name_plural = "Бронювання"

# Represents a review left by a participant after the tour
class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews', verbose_name="Тур")  # Tour being reviewed
    name = models.CharField(max_length=100, verbose_name="Ім'я")  # Name of the reviewer
    text = models.TextField(verbose_name="Відгук")  # Review text
    rating = models.PositiveSmallIntegerField(verbose_name="Оцінка")  # Rating from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")  # When the review was left

    def __str__(self):
        return f'Review by {self.name} – {self.rating}/5'  # Display format for review
    
    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"

class TourStop(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='stops', verbose_name="Тур")
    name = models.CharField(max_length=100, verbose_name="Назва точки")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Довгота")
    order = models.PositiveIntegerField(verbose_name="Порядок")

    class Meta:
        verbose_name = "Точка маршруту"
        verbose_name_plural = "Маршрутні точки"
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.name}"

