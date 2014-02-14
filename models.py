from django.db import models

from constants import errors

# Create your models here.
class UsersModel(models.Model):
	username = models.CharField(max_length=128, unique=True);
	password = models.CharField(max_length=128);
	count = models.IntegerField(default=1);

	def _init_(self):

	def addUser(user,pass):
		if not user
			return {'errCode':errors.ERR_BAD_USERNAME};

		if (UsersModel.objects.get(username=user):
			return {'errCode':errors.ERR_USER_EXISTS};
		else:
			UsersModel(username=user,password=pass).save();
			return {'errcode':errors.SUCCESS}

	def login(user,pass):
		dic1 = {}
		if not (UsersModel.objects.get(username=user):
			return {'errCode':errors.ERR_BAD_CREDENTIALS}

		dic1 = UsersModel.objects.get(username=user);

		if dic1.password != pass:
			return {'errCode':errors.ERR_BAD_CREDENTIALS}

		else:
			dic1.count +=1;
			dic1.save();
			return {'errCode': errors.SUCCESS};

	def resetFixture():
		UsersModel.objects.all().delete();
		return {'errCode': errors.SUCCESS};







