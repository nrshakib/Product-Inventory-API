from rest_framework import status
from rest_framework.response import Response


def api_response(message, data=None, status_code=status.HTTP_200_OK):
    return Response({
         "message": message,
         "status_text": "success",
         "data": data
    }, status=status_code)