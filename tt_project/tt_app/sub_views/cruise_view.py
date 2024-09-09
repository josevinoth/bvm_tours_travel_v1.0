from django.shortcuts import render
from ..forms import registrationaddForm

def cruise_view(request):
    reg_form = registrationaddForm()  # Create a new form instance
    context = {
        'reg_form': reg_form,
    }
    return render(request, 'tt_html/cruise.html', context)