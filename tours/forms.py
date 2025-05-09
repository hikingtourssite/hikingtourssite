from django import forms
from .models import Booking, Review

# Form for booking a tour
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'participants']
        labels = {
            'full_name': 'Прізвище, Ім’я',
            'email': 'Email',
            'participants': 'Кількість учасників',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'participants': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text', 'rating']
        labels = {
            'name': 'Ім’я',
            'text': 'Відгук',
            'rating': 'Оцінка',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }

