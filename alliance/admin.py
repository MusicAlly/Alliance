from django.contrib import admin
from django.db.models import TextField
from django.forms import TextInput

from alliance.models import *


if False:
    class AllianceAdmin(admin.ModelAdmin):
        using = 'alliance'

        def save_model(self, request, obj, form, change):
            obj.save(using=self.using)

        def delete_model(self, request, obj):
            obj.delete(using=self.using)

        def queryset(self, request):
            return super(AllianceAdmin, self).queryset(request).using(
                self.using)

        def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
            return super(AllianceAdmin, self).formfield_for_foreignkey(
                db_field, request=request, using=self.using, **kwargs)

        def formfield_for_manytomany(self, db_field, request=None, **kwargs):
            return super(AllianceAdmin, self).formfield_for_manytomany(
                db_field, request=request, using=self.using, **kwargs)
else:
    class AllianceAdmin(admin.ModelAdmin):
        pass


class RegionAdmin(AllianceAdmin):
    list_display = ('label',)
admin.site.register(Region, RegionAdmin)


class SkillAdmin(AllianceAdmin):
    list_display = ('label',)
admin.site.register(Skill, SkillAdmin)


class SkillLevelAdmin(AllianceAdmin):
    list_display = ('label',)
admin.site.register(SkillLevel, SkillLevelAdmin)


class UserSkillInline(admin.TabularInline):
    model = UserSkill

class UserProfileAdmin(AllianceAdmin):
    inlines = [UserSkillInline]
    list_display = ('user',)
admin.site.register(UserProfile, UserProfileAdmin)


class RequirementInline(admin.TabularInline):
    model = Requirement
    raw_id_fields = ('takers',)

class OpportunityAdmin(AllianceAdmin):
    inlines = [RequirementInline]
    list_display = ('label', 'owner', 'post_date')
    date_hierarchy = 'post_date'
admin.site.register(Opportunity, OpportunityAdmin)
