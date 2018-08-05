from .models import Branch, Post
from .serializers import BranchSerializer, PostOverviewSerializer

from django.conf import settings

from rest_framework import viewsets, generics
from rest_framework import exceptions


class BranchesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class PostsList(generics.ListAPIView):
    serializer_class = PostOverviewSerializer

    def get_queryset(self):
        branch_id = self.request.query_params.get('branch', None)
        if not branch_id:
            raise exceptions.ValidationError()

        try:
            branch = Branch.objects.get(pk=branch_id)
        except Branch.DoesNotExist:
            raise exceptions.ValidationError()

        page = int(self.request.query_params.get('page', 0))
        if page < 0:
            raise exceptions.ValidationError()

        all_branch_posts = Post.objects.filter(
            branch=branch).order_by('created_at')
        return all_branch_posts[
               settings.POSTS_IN_PAGE * page:settings.POSTS_IN_PAGE * (
                           page + 1)]


class PostRetrieve(generics.RetrieveAPIView):
    queryset = Post
    serializer_class = PostOverviewSerializer

