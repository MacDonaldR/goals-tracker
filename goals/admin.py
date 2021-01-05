from django.contrib import admin

from .models import Goal, Session, Milestone, Resource
# Register your models here.

admin.site.register(Goal)
admin.site.register(Session)
admin.site.register(Milestone)
admin.site.register(Resource)