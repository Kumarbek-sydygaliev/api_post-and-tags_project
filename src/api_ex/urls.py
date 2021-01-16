from django.urls import path,include
from .views import (
    home,

    PostListView, PostDetailView, PostCreateView, PostRemoveView,
    TagListView, TagDetailView, TagCreateView, TagRemoveView,

    main_view, 
    
    post_detail_view, post_create,
    tag_detail_view, tag_create,
    )

urlpatterns = [
    # path('', home),
    path('api_posts/', PostListView.as_view()),
    path('api_posts/<int:post_id>/', PostDetailView.as_view()),
    path('api_post/create', PostCreateView.as_view()),
    path('api_post/remove/<int:post_id>/', PostRemoveView.as_view()),

    path('api_tags/', TagListView.as_view()),
    path('api_tags/<int:tag_id>/', TagDetailView.as_view()),
    path('api_tag/create', TagCreateView.as_view()),
    path('api_tag/remove/<int:tag_id>/', TagRemoveView.as_view()),

    path('', main_view),

    path('posts/<int:post_id>/', post_detail_view),
    path('post/create', post_create),

    path('tags/<int:tag_id>/', tag_detail_view),
    path('tag/create', tag_create),
    ]
