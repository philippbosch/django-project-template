from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin


class CreatedByMixin(object):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        return super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.created_by = request.user
            instance.save()
        formset.save_m2m()


class SiteMixin(object):
    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        list_display += ('site',)
        return list_display

    def get_list_filter(self, request):
        list_filter = super().get_list_filter(request)
        list_filter += ('site',)
        return list_filter

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        readonly_fields += ('site',)
        return readonly_fields

    def save_model(self, request, obj, form, change):
        if not change:
            obj.site = request.site
        return super().save_model(request, obj, form, change)


class BaseAdmin(CreatedByMixin, SiteMixin, admin.ModelAdmin):
    pass


class BaseInlineAdmin(CreatedByMixin, InlineModelAdmin):
    pass
