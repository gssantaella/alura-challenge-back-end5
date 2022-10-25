from rest_framework import viewsets
from aluraflixbe.models import Video
from aluraflixbe.serializer import VideoSerializer


class VideosViewSet(viewsets.ModelViewSet):
    """
    Exibe todos os videos
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
