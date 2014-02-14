from models import UsersModel
from constants import errors
import json
from django.http import HttpResponse
from django.http import Http404

from django.views.decorators.csrf import csrf_exempt

from django import forms

def add(request):
	if request.method == 'POST':

		x = json.loads(request.body)
		err = {}

		user = x.get('username')
		password = x.get('password')

		if not user or len(user) > errors.MAX_USERNAME_LENGTH:
			err['errCode'] = errors.ERR_BAD_USERNAME
			return HttpResponse(json.dumps(err), content_type="application/json")

		if len(password)>constants.MAX_PASSWORD_LENGTH:
			err['errCode'] = errors.ERR_BAD_PASSWORD
			return HttpResponse(json.dumps(err), content_type="application/json")

		if UsersModel.addUser(user,password) == 1:
			err['errCode'] = errors.SUCCESS
			err['count'] = 1
			return HttpResponse(json.dumps(err), content_type="application/json")
		else:
			HttpResponse(json.dumps(UsersModel.addUser(user,password)), content_type="application/json")

def login(request):
	if request.method == 'POST':

		x = json.loads(request.body)
		err = {}

		user = x.get('username')
		password = x.get('password')

		if not user or len(user) > errors.MAX_USERNAME_LENGTH:
			err['errCode'] = errors.ERR_BAD_USERNAME
			return HttpResponse(json.dumps(err), content_type="application/json")

		if UsersModel.addUser(user,password) == 1:
			err['errCode'] = errors.SUCCESS
			err['count'] = UsersModel.objects.get(username=user).count;
			return HttpResponse(json.dumps(err), content_type="application/json")
		else:
			HttpResponse(json.dumps(UsersModel.login(user,password)), content_type="application/json")

	else:
		raise Http404

def resetFixture(request):
	if request.method == 'POST':
		UsersModel.resetFixture()
		err ={}
		err{'errCode'} = 1;
		return HttpResponse(json.dumps(err), content_type="application/json")

	else:
		raise Http404
			


