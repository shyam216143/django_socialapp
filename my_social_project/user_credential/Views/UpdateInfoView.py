from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from my_social_app.models import User
from my_social_app.renderers import UserRenderer
from serializers_data.Serializers.ProfileInfoSerializer import ProfileInfoSerializer
from serializers_data.Serializers.UserLoginSerializer import LoginDataSerializer



class UpdateInfoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, formate=None):
        user = request.data
        print("profile user is: ", user)
        serializer = ProfileInfoSerializer(data=request.data, context={'user': request.user})
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            print("serializer data is ", serializer.data)
            response = Response()
            response.data1 = request.data
            response.email = request.user.email
            data = User.objects.get(email=request.user.email)
            serializer1 = LoginDataSerializer(data, many=False)
            response.data = serializer1.data
            print(response.data1)

            return response
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
