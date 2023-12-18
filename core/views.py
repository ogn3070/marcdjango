from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView,RetrieveAPIView, DestroyAPIView
from .models import User, product
from .serializer import userSerializer, productSerializer
from rest_framework.permissions import IsAdminUser

class getUsers(ListAPIView):
  queryset = User.objects.all()
  serializer_class = userSerializer
  
class signup(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = userSerializer
  
  
class authentication(RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = userSerializer
  
class products(ListAPIView):
  queryset = product.objects.all()
  serializer_class = productSerializer

class singleproduct(RetrieveAPIView):
    queryset = product.objects.all()
    serializer_class = productSerializer
    
    
class deleteproduct(DestroyAPIView):
  queryset = product.objects.all()
  serializer_class = productSerializer
  permission_classes = [IsAdminUser]



