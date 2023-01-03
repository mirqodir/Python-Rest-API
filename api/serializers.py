from rest_framework import serializers
from my_app.models import User,Client

class UserSeralizers(serializers.ModelSerializer):
	class Meta:
		model = User
		# fields = '__all__' #qilib yozishimiz ham mumkin bunda hamma fieldlarni chiqarib beradi
		fields = ('FirstName','LastName','UserName','id') # bu kurinishdagi esa faqat biz xoxlaganlarini chiqarib beradi


class ClientSeralizers(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__' #qilib yozishimiz ham mumkin bunda hamma fieldlarni chiqarib beradi
		# fields = ('FirstName','LastName','CarModel','CarNumber','PhoneNumber','CreatedUserld') # bu kurinishdagi esa faqat biz xoxlaganlarini chiqarib beradi
