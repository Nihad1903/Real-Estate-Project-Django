from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

def get_all_instances(Model, Serializer):
    @api_view(["GET"])
    def view(request):
        items = Model.objects.all()
        serializer = Serializer(items, many=True)
        return Response(serializer.data)
    return view


def get_single_instance(Model, Serializer):
    @api_view(["GET"])
    def view(request, pk):
        try:
            item = Model.objects.get(id=pk)
        except Model.DoesNotExist:
            return Response({"detail": f"{Model.__name__} not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = Serializer(item, many=False)
        return Response(serializer.data)
    return view


def create_instance(Model, Serializer, ImageModel=None, image_field_name=None):
    @swagger_auto_schema(
        method='post',
        request_body=Serializer,
        operation_description=f"Create a new {Model.__name__}"
    )
    @api_view(["POST"])
    @permission_classes([IsAuthenticated])
    @parser_classes([MultiPartParser, FormParser])
    def view(request):
        data = request.data.copy()
        data['owner'] = request.user.id
        serializer = Serializer(data=data)

        if serializer.is_valid():
            item = serializer.save()

            if ImageModel and image_field_name:
                images = request.FILES.getlist('images')
                for image in images:
                    ImageModel.objects.create(**{image_field_name: item, 'image': image})

            return Response(Serializer(item).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return view


def edit_instance(Model, Serializer, ImageModel=None, image_field_name=None):
    @swagger_auto_schema(
        method='put',
        request_body=Serializer,
        operation_description=f"Edit an existing {Model.__name__}"
    )   
    @api_view(["PUT"])
    @permission_classes([IsAuthenticated])
    @parser_classes([MultiPartParser, FormParser])
    def view(request, pk):
        try:
            item = Model.objects.get(id=pk)
        except Model.DoesNotExist:
            return Response({"detail": f"{Model.__name__} not found."}, status=status.HTTP_404_NOT_FOUND)

        if item.owner != request.user:
            return Response({"detail": "Not authorized."}, status=status.HTTP_403_FORBIDDEN)

        data = request.data.copy()
        data['owner'] = request.user.id
        serializer = Serializer(instance=item, data=data, partial=True)

        if serializer.is_valid():
            updated_item = serializer.save()

            if ImageModel and image_field_name:
                images = request.FILES.getlist('images')
                if images:
                    ImageModel.objects.filter(**{image_field_name: item}).delete()
                    for image in images:
                        ImageModel.objects.create(**{image_field_name: item, 'image': image})

            return Response(Serializer(updated_item).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return view


def delete_instance(Model):
    @api_view(["DELETE"])
    @permission_classes([IsAuthenticated])
    def view(request, pk):
        try:
            item = Model.objects.get(id=pk)
        except Model.DoesNotExist:
            return Response({"detail": f"{Model.__name__} not found."}, status=status.HTTP_404_NOT_FOUND)

        if item.owner != request.user:
            return Response({"detail": "Not authorized."}, status=status.HTTP_403_FORBIDDEN)

        item.delete()
        return Response({"detail": f"{Model.__name__} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    return view
