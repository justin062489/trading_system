from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny  # NOQA
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from core.serializer import OrderSerializer, TotalValueSerializer
from core.models import Order


class OrderViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post',]

    @action(detail=False, methods=["post"], url_path=r'post-order',)
    def post_order(self, request):
        serializer = OrderSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], url_path=r'total-value',)
    def total_value(self, request):
        serializer = TotalValueSerializer(data=self.request.data,  context={'request':request} )
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    