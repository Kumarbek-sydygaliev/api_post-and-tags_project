import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)

from .models import Post, Tag
from .serializers import(
    PostListSerializer, PostDetailSerializer, PostCreateSerializer, PostRemoveSerializer,
    TagListSerializer, TagDetailSerializer, TagCreateSerializer, TagRemoveSerializer,
    )


def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def main_view(request):
    posts = Post.objects.all().order_by('-id')
    tags = Tag.objects.all().order_by('-id')
    return render(request, 'main_view.html', context={'posts':posts, 'tags':tags})

def post_detail_view(request, post_id):
    posts = Post.objects.all().order_by('-id')
    tags = Tag.objects.all().order_by('-id')

    post = Post.objects.get(pk=post_id)
    post_tags = post.tags.all()
    return render(request, 'post_detail.html', context={'post':post, 'post_tags':post_tags, 'posts':posts, 'tags':tags})

def post_create(request):
    posts = Post.objects.all().order_by('-id')
    tags = Tag.objects.all().order_by('-id')

    if request.GET:
        a = Post.objects.create(title=request.GET['title'], body=request.GET['body'])
        for i in dict(request.GET)['chosen_tags']:
            a.tags.add(Tag.objects.get(name=i).id)
        a.save()
    return render(request, 'post_create.html', context={'posts':posts, 'tags':tags})

def tag_create(request):
    posts = Post.objects.all().order_by('-id')
    tags = Tag.objects.all().order_by('-id')

    if request.GET:
        a = Tag.objects.create(name=request.GET['name'])
        for i in dict(request.GET)['chosen_posts']:
            a.post.add(Post.objects.get(title=i).id)
        a.save()
    return render(request, 'tag_create.html', context={'posts':posts, 'tags':tags})

def tag_detail_view(request, tag_id):
    posts = Post.objects.all().order_by('-id')
    tags = Tag.objects.all().order_by('-id')

    tag = Tag.objects.get(pk=tag_id)
    return render(request, 'tag_detail.html', context={'tag':tag, 'posts':posts, 'tags':tags})


class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class TagListView(ListAPIView):
    serializer_class = TagListSerializer
    queryset = Tag.objects.all()

class PostDetailView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk' # id
    lookup_url_kwarg = 'post_id'

class TagDetailView(RetrieveAPIView):
    serializer_class = TagDetailSerializer
    queryset = Tag.objects.all()
    lookup_field = 'pk' # id
    lookup_url_kwarg = 'tag_id'

class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer

class TagCreateView(CreateAPIView):
    serializer_class = TagCreateSerializer

class PostRemoveView(DestroyAPIView):
    serializer_class = PostRemoveSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'post_id'
    queryset = Post.objects.all()

class TagRemoveView(DestroyAPIView):
    serializer_class = TagRemoveSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'tag_id'
    queryset = Tag.objects.all()



#=== all posts view ===
# @api_view(['GET'])
# def all_posts(request):
#     posts = Post.objects.all()
#     # posts = [{'title':i.title, 'body':i.body} for i in posts]
#     ser = PostListSerializer(posts , many = True)


#=== all tags view ===
#     return Response(data = ser.data)
# @api_view(['GET'])
# def all_tags(request):
#     tags = Tag.objects.all()
#     ser = TagListSerializer(tags , many = True)
    # return Response(data = ser.data)


#=== new post create ===
# @api_view(['POST'])
# def post_create(request):
#     ser = PostCreateSerializer(data = request.data)
#     ser.is_valid(raise_exception=True)
#     Post.objects.create(**ser.data)
#     return Response(data = {"success":True,"message":"Post created"})


#=== new tag create ===
# @api_view(['POST'])
# def tag_create(request):
#     ser = TagCreateSerializer(data = request.data)
#     ser.is_valid(raise_exception=True)
#     Tag.objects.create(**ser.data)
#     return Response(data = {"success":True,"message":"Tag created"})


#=== post details view ===
# @api_view(['GET'])
# def post_details(request, post_id):
#     posts = Post.objects.get(id = post_id)
#     ser = PostDetailSerializer(posts)
#     return Response(data = ser.data)


#=== tag details view ===
# @api_view(['GET'])
# def tag_details(request, tag_id):
#     tags = Tag.objects.get(id = tag_id)
#     ser = TagDetailSerializer(tags)
#     return Response(data = ser.data)