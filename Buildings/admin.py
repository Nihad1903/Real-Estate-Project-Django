from django.contrib import admin
from .models import *
from django import forms


class FavoriteAdminForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Restrict content_type choices to only property models
        allowed_models = [Flat, GardenHouse, Garage, Land, Office]
        allowed_cts = ContentType.objects.get_for_models(*allowed_models).values()
        self.fields['content_type'].queryset = ContentType.objects.filter(id__in=[ct.id for ct in allowed_cts])

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    form = FavoriteAdminForm
    list_display = ('user', 'content_type', 'object_id', 'content_object', 'created_at')
    list_filter = ('content_type', 'created_at')
    search_fields = ('user__username', 'object_id')





class FlatImageInline(admin.TabularInline):
    model = FlatImage
    extra = 1

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    inlines = [FlatImageInline]



class GardenHouseImageInline(admin.TabularInline):
    model = GardenHouseImage
    extra = 1

@admin.register(GardenHouse)
class GardenHousetAdmin(admin.ModelAdmin):
    inlines = [GardenHouseImageInline]



class OfficeImageInline(admin.TabularInline):
    model = OfficeImage
    extra = 1

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    inlines = [OfficeImageInline]



class GarageImageInline(admin.TabularInline):
    model = GarageImage
    extra = 1

@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    inlines = [GarageImageInline]


class LandImageInline(admin.TabularInline):
    model = LandImage
    extra = 1

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    inlines = [LandImageInline]