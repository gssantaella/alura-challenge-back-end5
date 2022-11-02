from rest_framework import viewsets, filters, generics
from aluraflixbe.models import Video, Categoria
from aluraflixbe.serializer import VideoSerializer, CategoriaSerializer, ListaVideosPorCategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend


class VideosViewSet(viewsets.ModelViewSet):
    """
    Exibe todos os videos
    """
    queryset = Video.objects.all().order_by('id')
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['titulo']
    filterset_fields = ['categoria']


class CategoriasViewset(viewsets.ModelViewSet):
    """
    Exibe todas as categorias
    """
    queryset = Categoria.objects.all().order_by('id')
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['titulo', 'cor']


class ListaVideosPorCategoria(generics.ListAPIView):
    """
    Listando videos por tipo de categoria
    """
    def get_queryset(self):
        return Video.objects.filter(categoria_id=self.kwargs['pk'])
    serializer_class = ListaVideosPorCategoriaSerializer
