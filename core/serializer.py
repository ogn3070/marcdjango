from rest_framework import serializers
from .models import User, product
from django.contrib.auth.hashers import make_password

class userSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
  
  def create(self, validated_data):
    validated_data['password'] = make_password(validated_data['password'])
    validated_data['is_active'] = True
    
    return super().create(validated_data)
  




class productSerializer(serializers.ModelSerializer):
  class Meta:
    model = product
    fields = '__all__'
    
  
  
