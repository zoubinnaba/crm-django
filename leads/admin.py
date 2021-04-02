from django.contrib import admin

from leads.models import (
    User,
    Lead,
    Agent,
    UserProfile,
    Category
)


class LeadAdmin(admin.ModelAdmin):
    # fields = (
    #     'first_name',
    #     'last_name'
    # )
    list_display = ['first_name', 'last_name', 'age', 'email']
    list_filter = ['category']
    search_fields = ['first_name', 'last_name']


admin.site.register(User)
admin.site.register(Lead, LeadAdmin)
admin.site.register(Agent)
admin.site.register(UserProfile)
admin.site.register(Category)
