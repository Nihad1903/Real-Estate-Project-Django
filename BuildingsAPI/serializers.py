from rest_framework import serializers
from Buildings.models import *

class FavoriteSerializer(serializers.ModelSerializer):
    content_type = serializers.SlugRelatedField(
        slug_field='model',
        queryset=ContentType.objects.all()
    )

    class Meta:
        model = Favorite
        fields = ['id', 'content_type', 'object_id', 'created_at']



class FlatImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = FlatImage
        fields = ['image']

class FlatSerializer(serializers.ModelSerializer):
    flat_images = FlatImageSerializer(many=True, read_only=True)
    class Meta:
        model = Flat
        fields = '__all__'


class GardenHouseImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = GardenHouseImage
        fields = ['image']

class GardenHouseSerializer(serializers.ModelSerializer):
    garden_house_images = GardenHouseImageSerializer(many=True, read_only=True)
    class Meta:
        model = GardenHouse
        fields = '__all__'


class  OfficeImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = OfficeImage
        fields = ['image']

class OfficeSerializer(serializers.ModelSerializer):
    office_images = OfficeImageSerializer(many=True, read_only=True)
    class Meta:
        model = Office
        fields = '__all__'


class GarageImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = GarageImage
        fields = ['image']

class GarageSerializer(serializers.ModelSerializer):
    garage_images = GarageImageSerializer(many=True, read_only=True)
    class Meta:
        model = Garage
        fields = '__all__'


class LandImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = LandImage
        fields = ['image']

class LandSerializer(serializers.ModelSerializer):
    land_images = LandImageSerializer(many=True, read_only=True)
    class Meta:
        model = Land
        fields = '__all__'