import requests
from django.http import JsonResponse
from rest_framework import generics

postsEndpoint='https://jsonplaceholder.typicode.com/posts'
commentsEndpoint='https://jsonplaceholder.typicode.com/comments'

def getData(endpoint):
    response=requests.get(endpoint)
    return response.json()

class Top_Posts(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        posts=getData(postsEndpoint)
        comments=getData(commentsEndpoint)
        top_posts=[]
        for post in posts:
            postComments=[i for i in comments if i['postId']==post['id']]
            top_posts.append({
                'postId': post['id'],
                'post_title': post['title'],
                'post_body': post['body'],
                'total_number_of_comments': len(postComments)
            })
        top_posts_sorted=sorted(top_posts, key=lambda x: -x['total_number_of_comments'])
        return JsonResponse(top_posts_sorted, safe=False)

class Search_Comments(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        comments=getData(commentsEndpoint)
        for key in request.data:
            comments=[i for i in comments if i[key]==request.data[key]]
        print(comments)
        return JsonResponse(comments, safe=False)
