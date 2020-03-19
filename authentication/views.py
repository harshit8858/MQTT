from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.utils import request_type, jsontype


class LoginApi(APIView):
    """
    Login/signup api
    Parameters:mobile
    Returns:Otp
    """

    def post(self, request):
        data = request_type(request)
        return Response({'res': 1, 'msg': 'Done!'})
