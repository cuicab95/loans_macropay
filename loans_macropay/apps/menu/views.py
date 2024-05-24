from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Menu
from .serializers import MenuSerializer
from .services import MenuServices

# Create your views here.
class MenuViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated, ]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    service = MenuServices

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = self.service.build_menu_tree(queryset)
        return Response(data)

    def create(self, request, *args, **kwargs):
        menu_list = request.data
        menu_list = sorted(menu_list, key=lambda x: x['parent_id'] if x['parent_id'] else 0, reverse=False)
        for menu_data in menu_list:
            serializer = self.get_serializer(data=menu_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)

