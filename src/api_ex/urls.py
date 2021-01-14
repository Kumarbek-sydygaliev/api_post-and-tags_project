from django.urls import path,include
from .views import (
    home,

    PostListView, PostDetailView, PostCreateView, PostRemoveView,
    TagListView, TagDetailView, TagCreateView, TagRemoveView,

    posts_view, post_detail_view, post_create,
    tag_view,
    )

urlpatterns = [
    # path('', home),
    path('api_posts/', PostListView.as_view()),
    path('api_posts/<int:post_id>/', PostDetailView.as_view()),
    path('api_post/create', PostCreateView.as_view()),
    path('post/remove/<int:post_id>/', PostRemoveView.as_view()),

    path('tags/', TagListView.as_view()),
    path('api_tags/<int:tag_id>/', TagDetailView.as_view()),
    path('tag/create', TagCreateView.as_view()),
    path('tag/remove/<int:tag_id>/', TagRemoveView.as_view()),

    path('posts/', posts_view),
    path('posts/<int:post_id>/', post_detail_view),
    path('post/create', post_create),

    path('tags/<int:tag_id>/', tag_view),
    ]
