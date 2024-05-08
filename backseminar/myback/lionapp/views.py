from django.shortcuts import render
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import *

from django.http import HttpResponse

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

def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        'id': post.pk,
        '제목': post.title,
        '내용': post.content,
        '메시지': '조회 성공'
    }
    return JsonResponse(data, status=200)

def delete_post(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        data = {
            "message" : f"id: {pk} 포스트 삭제 완료"
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})

def get_comment(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        comment_list = post.comments.all()
        return HttpResponse(comment_list, status=200)

#user_id와 post_id를 request로 받고 좋아요를 누르는 api
#( response는 204 no content로 반환 )
def like(request, user_id, post_id):
    if request.method == 'PATCH':
        post = get_object_or_404(Post, pk=post_id)
        post.user_posts.user_id = user_id
        post.like_count += 1
        post.save()
        data = {
            "message" : f"id: {post_id} 좋아요 수 증가"
        }
        return JsonResponse(data, status=204)

#post_id를 request로 받아 좋아요 개수를 반환하는 api
#( response는 like_count : 1 )
def get_likes(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)

        return JsonResponse({'message':f'{post_id}의 총 하트 수는 {post.like_count}입니다.'})

#댓글이 많이 달린 순으로 post를 정렬하여 리스트로 반환하는 api
#( response로는 comment_list를 반환한 것처럼 post에서 __str__에 정의된 값으로 리스트화해서 반환 )
def sort_post(request):
    if request.method == 'GET':
        post_list = Post.objects.all().order_by('-like_count')
        return HttpResponse(post_list, status=200)

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