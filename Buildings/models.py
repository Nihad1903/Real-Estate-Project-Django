from django.db import models
import uuid
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from Buildings.utils.upload_paths import *

category_choices = [
    ("NB", "New Building"),
    ("OB", "Old Building")
]
announcement_choices = [
    ("S", "Sale"),
    ("R", "Rent")
]
office_choices = [
    ("H/F", "House, Flat"),
    ("BC", "Business Center")
]

class Favorite(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='favorites')
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_id')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')  

    def __str__(self):
        return f"{self.user} -> {self.content_object}"


class BaseProperty(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=350, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    about = models.TextField(max_length=2000, null=True, blank=True)
    area = models.IntegerField(null=True, blank=True)
    location = models.TextField(max_length=300, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    
class Flat(BaseProperty):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='flats', null=True)
    announcement_type = models.CharField(null=True, blank=True, max_length=200,
                                         choices=announcement_choices)
    room_num = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(null=True, blank=True)
    new = models.BooleanField(null=True, blank=True)
    repair = models.BooleanField(null=True, blank=True)
    mortgage = models.BooleanField(null=True, blank=True)
    category = models.CharField(null=True, blank=True, max_length=200, choices=category_choices)

    def __str__(self):
        return f"{self.title}"


class FlatImage(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='flat_images')
    image = models.ImageField(upload_to=flat_image_upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.flat.id}"


class GardenHouse(BaseProperty):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='gardenhouses', null=True)
    announcement_type = models.CharField(null=True, blank=True, max_length=200,
                                         choices=announcement_choices)
    room_num = models.IntegerField(blank=True, null=True)
    land_area = models.IntegerField(null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    new = models.BooleanField(null=True, blank=True)
    repair = models.BooleanField(null=True, blank=True)
    mortgage = models.BooleanField(null=True, blank=True)
    category = models.CharField(null=True, blank=True, max_length=200, choices=category_choices)

    def __str__(self):
        return f"{self.title}"


class GardenHouseImage(models.Model):
    garden_house = models.ForeignKey(GardenHouse, on_delete=models.CASCADE, related_name='garden_house_images')
    image = models.ImageField(upload_to=garden_house_image_upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.garden_house.id}"
    

class Office(BaseProperty):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='offices', null=True)
    announcement_type = models.CharField(null=True, blank=True, max_length=200,
                                         choices=announcement_choices)
    room_num = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(null=True, blank=True)
    new = models.BooleanField(null=True, blank=True)
    repair = models.BooleanField(null=True, blank=True)
    category = models.CharField(null=True, blank=True, max_length=200, choices=office_choices)

    def __str__(self):
        return f"{self.title}"


class OfficeImage(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='office_images')
    image = models.ImageField(upload_to=office_image_upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.office.id}"


class Garage(BaseProperty):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='garages', null=True)
    extract = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class GarageImage(models.Model):
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, related_name="garage_images")
    image = models.ImageField(upload_to=garage_image_upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.garage.id}"


class Land(BaseProperty):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='lands', null=True)
    extract = models.BooleanField(null=True, blank=True)
    mortgage = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class LandImage(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name="land_images")
    image = models.ImageField(upload_to=land_image_upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.land.id}"
