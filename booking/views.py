from django.shortcuts import render
from django.http import JsonResponse

# Sample seat layout
seat_layout = [
    ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10'],
    ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10'],
    ['C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C10'],
    ['D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10'],
]

ticket_price = 100000  # 100,000 VND per seat

def index(request):
    return render(request, 'booking/index.html', {'seat_layout': seat_layout, 'ticket_price': ticket_price})

def confirm_selection(request):
    selected_seats = request.POST.getlist('seats')
    total_price = len(selected_seats) * ticket_price
    return JsonResponse({'selected_seats': selected_seats, 'total_price': total_price})
