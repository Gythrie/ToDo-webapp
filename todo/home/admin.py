from django.contrib import admin
from home.models import Tasks

# Register your models here.



class TaskAdmin(admin.ModelAdmin):
    list_display = ('taskTitle', 'taskDesc', 'approved')
    actions = ['approve_tasks']

    def approve_tasks(self, request, queryset):
        updated_count = queryset.update(approved=True)
        self.message_user(request, f'{updated_count} task(s) successfully approved.')

    approve_tasks.short_description = "Approve selected tasks"


# def approve_tasks(modeladmin, request, queryset):
#     queryset.update(approve=True)

# approve_tasks.short_description = "Approve selected tasks"

# @admin.register(Tasks)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('taskTitle', 'taskDesc', 'approved')
#     actions = [approve_tasks]

admin.site.register(Tasks,TaskAdmin)    
