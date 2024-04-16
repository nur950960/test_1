from rest_framework import serializers 
from django.contrib.auth import get_user_model  
from django.contrib.auth.password_validation import validate_password

User = get_user_model() 

class RegisterSerializer(serializers.ModelSerializer): 
    password = serializers.CharField(min_length=8, max_length=10, required=True, write_only=True)
    password2 = serializers.CharField(min_length=8, max_length=10, required=True, write_only=True)

    class Meta:
        model = User 
        fields = '__all__' 

    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs.pop('password2')

        if password2 != password: 
            raise serializers.ValidationError('Пароли не совпадают') 
        validate_password(password) 
        return attrs 
    
    def create(self, validated_data):
        password = validated_data['password']
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save() 
        return user 