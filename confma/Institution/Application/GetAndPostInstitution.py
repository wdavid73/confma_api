from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.Institution import Institution
from ..Infractructure.SerializerInstitution import SerializerInstitution


class GetAndPost(APIView):

    def get(self, request: Request):
        institution = Institution.objects.filter(state=1)
        serializer = SerializerInstitution(
            institution, many=True, context={'request': request})
        return Response({"institutions": serializer.data})

    def post(self, request: Request):
        serializer = SerializerInstitution(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
