from rest_framework import serializers
from .models import CarModel, FeedBack
from django.core.mail import send_mail

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
        car = self.validated_data['car']
        damage_description = self.validated_data['damage_description']
        contact_info = self.validated_data['contact_info']
        year = self.validated_data['year']

        message = "Пользователь с email: "+ email +"\nКонтактные данные:"+ contact_info + "\nАвтомобиль:"+ str(car)+ "\nГод авто:" + str(year) + "\nОписание повреждения и расчет стоимости:" + damage_description

        send_mail("Заявка отправлена в обработку. @Atlant M", "С вами свзяжется менеджер!", 'dolganov045@gmail.com', [email], fail_silently=False)
        send_mail("Заполнена форма обратной связи Кузовного ремонта. @Atlant M", message, 'dolganov045@gmail.com', ['stefaniya11092002@gmail.com'],fail_silently=False)


        print(damage_description)
        return feedback





