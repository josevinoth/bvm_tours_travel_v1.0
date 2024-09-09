from django.shortcuts import render
from ..forms import registrationaddForm
def wedding_jaipur_view(request):
    reg_form = registrationaddForm()
    context = {
        'reg_form': reg_form,
    }
    return render(request, 'tt_html/wedding_jaipur.html')