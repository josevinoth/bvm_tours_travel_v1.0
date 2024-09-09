from django.shortcuts import render
from ..forms import registrationaddForm

def wedding_agra_view(request):
    reg_form = registrationaddForm()
    context = {
        'reg_form': reg_form,
    }
    return render(request, 'tt_html/wedding_agra.html', context)