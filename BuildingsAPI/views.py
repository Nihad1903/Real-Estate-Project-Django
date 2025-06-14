from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import *  
from Buildings.models import *
from .utils import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_favorite(request):
    content_type_str = request.data.get('content_type')
    object_id = request.data.get('object_id')

    if not content_type_str or not object_id:
        return Response({'error': 'content_type and object_id are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        content_type = ContentType.objects.get(model=content_type_str)
    except ContentType.DoesNotExist:
        return Response({'error': 'Invalid content_type.'}, status=status.HTTP_400_BAD_REQUEST)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=object_id
    )

    if created:
        return Response({'message': 'Added to favorites.'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Already in favorites.'}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_favorite(request):
    content_type_str = request.data.get('content_type')
    object_id = request.data.get('object_id')

    if not content_type_str or not object_id:
        return Response({'error': 'content_type and object_id are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        content_type = ContentType.objects.get(model=content_type_str)
        favorite = Favorite.objects.get(user=request.user, content_type=content_type, object_id=object_id)
        favorite.delete()
        return Response({'message': 'Removed from favorites.'}, status=status.HTTP_204_NO_CONTENT)
    except (ContentType.DoesNotExist, Favorite.DoesNotExist):
        return Response({'error': 'Favorite not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    serializer = FavoriteSerializer(favorites, many=True)
    return Response(serializer.data)

# FLAT
get_flats = get_all_instances(Flat, FlatSerializer)
get_flat = get_single_instance(Flat, FlatSerializer)
create_flat = create_instance(Flat, FlatSerializer, FlatImage, 'flat')
edit_flat = edit_instance(Flat, FlatSerializer, FlatImage, 'flat')
delete_flat = delete_instance(Flat)

# GARDEN HOUSE
get_gardenhouses = get_all_instances(GardenHouse, GardenHouseSerializer)
get_gardenhouse = get_single_instance(GardenHouse, GardenHouseSerializer)
create_gardenhouse = create_instance(GardenHouse, GardenHouseSerializer, GardenHouseImage, 'garden_house')
edit_gardenhouse = edit_instance(GardenHouse, GardenHouseSerializer, GardenHouseImage, 'garden_house')
delete_gardenhouse = delete_instance(GardenHouse)

# OFFICE
get_offices = get_all_instances(Office, OfficeSerializer)
get_office = get_single_instance(Office, OfficeSerializer)
create_office = create_instance(Office, OfficeSerializer, OfficeImage, 'office')
edit_office = edit_instance(Office, OfficeSerializer, OfficeImage, 'office')
delete_office = delete_instance(Office)

# GARAGE
get_garages = get_all_instances(Garage, GarageSerializer)
get_garage = get_single_instance(Garage, GarageSerializer)
create_garage = create_instance(Garage, GarageSerializer, GarageImage, 'garage')
edit_garage = edit_instance(Garage, GarageSerializer, GarageImage, 'garage')
delete_garage = delete_instance(Garage)

# LAND
get_lands = get_all_instances(Land, LandSerializer)
get_land = get_single_instance(Land, LandSerializer)
create_land = create_instance(Land, LandSerializer, LandImage, 'land')
edit_land = edit_instance(Land, LandSerializer, LandImage, 'land')
delete_land = delete_instance(Land)
