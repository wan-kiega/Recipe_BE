from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call DRF's default handler first
    response = exception_handler(exc, context)

    if response is not None:
        # Standardize error format
        return Response({
            "success": False,
            "errors": response.data,
            "status_code": response.status_code,
        }, status=response.status_code)

    # Handle unexpected errors
    return Response({
        "success": False,
        "errors": {"detail": "Internal server error"},
        "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
