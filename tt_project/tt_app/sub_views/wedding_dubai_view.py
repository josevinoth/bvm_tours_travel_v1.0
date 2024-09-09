from django.shortcuts import render
from ..forms import registrationaddForm

def wedding_dubai_view(request):
    reg_form = registrationaddForm()  # Create a new form instance
    context = {
        'reg_form': reg_form,
    }
    return render(request, 'tt_html/wedding_dubai.html', context)
