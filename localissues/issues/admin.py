from django.contrib import admin
from .models import Issue, LocalLegislation, Option,Response, Question,Poll

# Register your models here.


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)
    pass


@admin.register(LocalLegislation)
class LocalLegislationAdmin(admin.ModelAdmin):
    pass

@admin.register(Option)
class Option(admin.ModelAdmin):
    pass

@admin.register(Response)
class Responce(admin.ModelAdmin):
    pass

@admin.register(Question)
class Question(admin.ModelAdmin):
    pass

@admin.register(Poll)
class Poll(admin.ModelAdmin):
    pass