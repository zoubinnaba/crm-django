from django.shortcuts import render
from leads.models import (
    Lead,
)


def home_page(request):
    leads = Lead.objects.all()
    return render(request, 'leads/home_page.html', {
        "leads": leads
    })