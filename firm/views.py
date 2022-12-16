from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item, Firm, Category
from rest_framework import viewsets, status
from .serializers import ItemSerializer, FirmSerializer, CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


@api_view(['GET', 'POST' ])
def firm_view(request):
    if request.method == 'GET':
        firm = Firm.objects.all()
        serializer = FirmSerializer(firm, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = FirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE' ])
def firm_detail(request, id):
    firm = get_object_or_404(Firm, id=id)
    if request.method == 'GET':
        serializer = FirmSerializer(firm)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = FirmSerializer(firm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        firm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryAPIView(APIView):

    def get(self, request, *args, **kwargs):
        items = Category.objects.all()
        serializer = CategorySerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetailAPIView(APIView):
    def get_object(self):
        return get_object_or_404(Category, id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        serializer = CategorySerializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer = CategorySerializer(self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)