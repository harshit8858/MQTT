from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.utils import request_type, jsontype


class LoginApi(APIView):
    def post(self, request):
        return Response({'res': 1, 'msg': 'Done!'})
