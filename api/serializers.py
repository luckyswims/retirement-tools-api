# import serializers from the django rest framework
from rest_framework import serializers

# import model
from .models import Annuity

# Create serializer class
# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class AnnuitySerializer(serializers.ModelSerializer):
    # Define meta class
    class Meta:
        # Specify the model from which to define the fields
        model = Annuity
        # Define fields to be returned
        fields = '__all__'
