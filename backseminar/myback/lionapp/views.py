from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.shortcuts import get_object_or_404
from .models import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView,View
from rest_framework.decorators import api_view
from .serializers import PostSerializer

from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

@swagger_auto_schema(
        method="POST", 
        tags=["첫번째 view"],
        operation_summary="post 생성", 
        operation_description="post를 생성합니다.",
        responses={
            201: '201에 대한 설명', 
            400: '400에 대한 설명',
            500: '500에 대한 설명'
        }
)

@authentication_classes([JWTAuthentication])
@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        title = data.get('title')
        content = data.get('content')

        post = Post(
            title = title,
            content = content
        )
        post.save()
        return JsonResponse({'message':'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})

@authentication_classes([JWTAuthentication])
@api_view(['GET'])
def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        'id': post.pk,
        '제목': post.title,
        '내용': post.content,
        '메시지': '조회 성공'
    }
    return JsonResponse(data, status=200)

@authentication_classes([JWTAuthentication])
@api_view(['DELETE'])
def delete_post(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        data = {
            "message" : f"id: {pk} 포스트 삭제 완료"
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})

@authentication_classes([JWTAuthentication])
@api_view(['GET'])
def get_comment(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        comment_list = post.comments.all()
        return HttpResponse(comment_list, status=200)
    

def api_response(data, message, status):
    response = {
        "message":message,
        "data":data
    }
    return Response(response, status=status)


@authentication_classes([JWTAuthentication])
@api_view(['POST'])
def create_post_v2(request):
    post = Post(
        title = request.data.get('title'),
        content = request.data.get('content')
    )
    post.save()

    message = f"id: {post.pk}번 포스트 생성 성공"
    return api_response(data = None, message = message, status = status.HTTP_201_CREATED)


class PostApiView(APIView):
    authentication_classes = [JWTAuthentication]
    def get_object(self, pk):
        post = get_object_or_404(Post, pk=pk)
        return post

    def get(self, request, pk):
        post = self.get_object(pk)

        postSerializer = PostSerializer(post)
        message = f"id: {post.pk}번 포스트 조회 성공"
        return api_response(data = postSerializer.data, message = message, status = status.HTTP_200_OK)
    
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        
        message = f"id: {pk}번 포스트 삭제 성공"
        return api_response(message = message, status = status.HTTP_200_OK) 

@authentication_classes([JWTAuthentication])    
@api_view(['PATCH'])    
def like(request, user_id, post_id):
    if request.method == 'PATCH':
        if UserPost.objects.filter(user_id=user_id, post_id=post_id).exists():
            return HttpResponse("Already exists.", status=409)
        else:
             user = Member.objects.get(pk = user_id)
        post = Post.objects.get(pk = post_id)

        userPost = UserPost(
            user_id = user,
            post_id = post
        )
        userPost.save()

        return HttpResponse(status=204)
    
@authentication_classes([JWTAuthentication])
@api_view(['GET'])       
def get_likes(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        like_count = UserPost.objects.filter(post_id=post_id).count()
        return JsonResponse({'message':f'{post_id}의 총 하트 수는 {like_count}입니다.'})

@authentication_classes([JWTAuthentication])
@api_view(['GET'])
def sort_post(request):
    if request.method == 'GET':
       post_list = Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count') 
       return HttpResponse(post_list, status=200)

@authentication_classes([JWTAuthentication])    
@api_view(['POST'])
def create_member(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data.get('name')
        email = data.get('email')

        member = Member(
            name = name,
            email = email
        )

        member.save()
        return JsonResponse({'message':'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})