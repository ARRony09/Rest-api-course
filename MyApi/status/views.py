from .models import StatusModel
from .serializers import StatusSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.


# class StatusCreateListApiView(mixins.CreateModelMixin, ListAPIView):
#     queryset = StatusModel.objects.all()
#     serializer_class = StatusSerializers

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class StatusCreateListApiView(ListCreateAPIView):
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializers

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class StatusDetailUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializers
    lookup_field = 'id'


# Using Mixins

# class StatusDetailUpdateDestroyApiView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, RetrieveAPIView):
#     queryset = StatusModel.objects.all()
#     serializer_class = StatusSerializers
#     lookup_field = 'id'

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(self, request, *args, **kwargs)


# class StatusUpdateApiView(UpdateAPIView):
#     queryset = StatusModel.objects.all()
#     serializer_class = StatusSerializers
#     lookup_field = 'id'


# class StatusDeleteApiView(DestroyAPIView):
#     queryset = StatusModel.objects.all()
#     serializer_class = StatusSerializers
#     lookup_field = 'id'
