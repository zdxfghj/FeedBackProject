from rest_framework import serializers
from .models import CarModel, FeedBack


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'

    def save(self):
        feedback = FeedBack.objects.create(**self.validated_data)
        email = self.validated_data['email']
        # send_email()
        return feedback

