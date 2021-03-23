from django.urls import path
from leads.views import (
    lead_list,
    lead_detail,
    lead_create
)

app_name = "leads"

urlpatterns = [
    path('', lead_list, name="lead_list"),
    path('lead_create/', lead_create, name="lead_create"),
    path('<pk>/', lead_detail, name="lead_detail"),
]
