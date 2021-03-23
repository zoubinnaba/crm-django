from django.shortcuts import render, redirect
from leads.models import (
    Lead,
    Agent,
    User
)
from leads.forms import LeadForm


def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/lead_list.html', {
        "leads": leads
    })
    
def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, 'leads/lead_detail.html',{
        "lead": lead
    })
    
def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # age = form.cleaned_data['age']
            # agent = form.cleaned_data['agent']
            # Lead.objects.create(
            #     first_name=first_name,
            #     last_name=last_name,
            #     age=age,
            #     agent=agent
            # )
            form.save()
            return redirect("leads:lead_list")
    return render(request, 'leads/lead_create.html',{
        "form": form
    })