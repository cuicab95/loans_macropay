from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProcessPaymentSerializer
from rest_framework.response import Response
from .models import Loans

# Create your views here.
class ProcessPaymentViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ProcessPaymentSerializer
    queryset = Loans.objects.none()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # exec SP
        return Response(serializer.data, status=status.HTTP_201_CREATED)

