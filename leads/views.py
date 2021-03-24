from django.shortcuts import render, redirect, reverse 
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from leads.models import (
    Lead,
    Agent,
    User
)
from leads.forms import LeadModelForm


class LandingPageView(TemplateView):
    template_name = "landing.html"



class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"



class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def  get_success_url(self):
        return reverse("leads:lead_list")
        


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(request.POST, instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return reverse("leads:lead_list")
#     return render(request, "leads/lead_update.html", {"form": form, "lead": lead})

class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    
    def  get_success_url(self):
        return reverse("leads:lead_list")
    

class LeadDeleteView(DeleteView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    
    def  get_success_url(self):
        return reverse("leads:lead_list")

