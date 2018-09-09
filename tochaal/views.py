from django.conf import settings
from django.core.paginator import Paginator

from .models import Subchaal, Thread
from .serializers import ThreadOverviewSerializer
from rest_framework import exceptions, generics, viewsets
from tochaal.serializers import SubchaalSerializer


class SubchaalsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subchaal.objects.all()
    serializer_class = SubchaalSerializer


class ThreadsList(generics.ListAPIView):
    serializer_class = ThreadOverviewSerializer

    def get_queryset(self):
        subchaal_id = self.request.query_params.get('subchaal', None)
        if not subchaal_id:
            raise exceptions.ValidationError()

        try:
            subchaal = Subchaal.objects.get(pk=subchaal_id)
        except Subchaal.DoesNotExist:
            raise exceptions.ValidationError()

        page_num = int(self.request.query_params.get('page', 0)) + 1
        if page_num < 1:
            raise exceptions.ValidationError()

        all_subchaal_threads = Thread.objects.filter(
            subchaal=subchaal).order_by('created_at')
        paginator = Paginator(all_subchaal_threads, settings.THREADS_IN_PAGE)
        return paginator.page(page_num).object_list


class ThreadRetrieve(generics.RetrieveAPIView):
    queryset = Thread
    serializer_class = ThreadOverviewSerializer
