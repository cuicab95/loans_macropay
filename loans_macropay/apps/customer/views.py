from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProcessPaymentSerializer
from rest_framework.response import Response
from .models import Loans
from django.db import connection

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
        result_payments = []
        result_customer = []
        with connection.cursor() as cursor:
            cursor.callproc('sp_process_payments', [serializer.validated_data['current_date'], serializer.validated_data['interest_rate'], serializer.validated_data['commercial_year_days']])
            results = cursor.fetchall()
            customers_id_list = []
            for data in results:
                result_payments.append({'Cliente': data[1], 'Plazo': data[3], 'Monto': data[4], 'Interés': data[5], 'IVA': data[6], 'Pago': data[7]})
                if data[2] not in customers_id_list:
                    result_customer.append({'Cliente': data[1], 'Monto': data[8]})
        return Response({'Pagos': result_payments, 'Cuentas': result_customer}, status=status.HTTP_201_CREATED)

