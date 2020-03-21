from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.utils import request_type, jsontype
from django.contrib.auth import authenticate
from .models import Client
from django.db import transaction


class RegisterApi(APIView):
    def post(self, request):
        try:
            data = request_type(request)
            name = data['name']
            name_ = name.split(' ')
            first_name = name_[0]
            last_name = ''
            if len(name_) > 1:
                for i in range(1, len(name_)):
                    last_name = last_name + name_[i]
            email = data['email']
            phone = data['phone']
            password = data['password']
            with transaction.atomic():
                user = User.objects.create(username='eiognnergireifo', first_name=first_name, last_name=last_name,
                                           email=email)
                user.username = user.first_name.lower() + '-' + str(user.id)
                user.set_password(password)
                user.save()
                clients = Client.objects.filter(phone=phone)
                if not clients.exists():
                    Client.objects.create(user=user, name=name, phone=phone)
                else:
                    return Response({'status': 0, 'msg': 'Phone number already exists!'})
            status = 1
            msg = 'Saved!'
        except Exception as e:
            print(e)
            status = 0
            msg = e
        return Response({'status': status, 'msg': msg})


class LoginApi(APIView):
    def post(self, request):
        data = request_type(request)
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            status = 1
            msg = 'Authenticated!'
        else:
            status = 0
            msg = 'Authencation failed!'
        return Response({'status': status, 'msg': msg})
