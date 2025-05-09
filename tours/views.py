from .models import Booking 
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Tour
from .forms import BookingForm, ReviewForm

# View to display list of all tours (used on homepage)
def tour_list(request):
    tours = Tour.objects.all()  # Get all tours from the database
    return render(request, 'tours/tour_list.html', {'tours': tours})

# View to show tour details and allow adding reviews
def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    reviews = tour.reviews.all().order_by('-created_at')
    review_form = ReviewForm()

    # Збір маршрутних точок
    stops = tour.stops.all()
    route = [{"name": stop.name, "lat": stop.latitude, "lon": stop.longitude} for stop in stops]

    # Обробка форми відгуку
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.tour = tour
            review.save()
            return HttpResponseRedirect(reverse('tour_detail', args=[pk]))

    return render(request, 'tours/tour_detail.html', {
        'tour': tour,
        'reviews': reviews,
        'review_form': review_form,
        'route': route,  # ⬅️ додаємо маршрут у шаблон
    })

# View to handle booking form for a specific tour
def book_tour(request, pk):
    tour = get_object_or_404(Tour, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  # Don't save yet, add extra data first
            booking.tour = tour  # Link booking to the selected tour
            if request.user.is_authenticated:
                booking.user = request.user  # Link booking to the logged-in user
            booking.save()
            return render(request, 'tours/booking_success.html', {'tour': tour})
    else:
        form = BookingForm()

    return render(request, 'tours/book_tour.html', {'form': form, 'tour': tour})

# View to show list of bookings made by the logged-in user
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('tour').order_by('-created_at')
    return render(request, 'tours/my_bookings.html', {'bookings': bookings})