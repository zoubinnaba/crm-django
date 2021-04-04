from django.urls import path
from leads.views import (
    LeadListView,
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView,
    LeadDeleteView,
    AssignedAgentView,
    CategoryListView,
    CategoryDetailView,
    LeadCategoryUpdateView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    LeadJsonView, FollowUpCreateView,
    FollowUpUpdateView, FollowUpDeleteView
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead_list"),
    path('json/', LeadJsonView.as_view(), name="lead_list-json"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead_detail"),
    path('<int:pk>/update', LeadUpdateView.as_view(), name="lead_update"),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name="lead_delete"),
    path('<int:pk>/assign-agent/', AssignedAgentView.as_view(), name="assign_agent"),
    path('<int:pk>/category/', LeadCategoryUpdateView.as_view(), name="lead_category_update"),
    path('<int:pk>/followups/create/', FollowUpCreateView.as_view(), name="lead_followup_create"),
    path('followups/<int:pk>/', FollowUpUpdateView.as_view(), name="lead_followup_update"),
    path('followups/<int:pk>/delete/', FollowUpDeleteView.as_view(), name="lead_followup_delete"),
    path('create/', LeadCreateView.as_view(), name="lead_create"),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete', CategoryDeleteView.as_view(), name='category_delete'),
    path('create-category/', CategoryCreateView.as_view(), name="category_create"),
]
