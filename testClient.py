import requests

def getTopPosts():
    endpoint='http://127.0.0.1:8000/backend_test/top_posts/'
    response=requests.get(endpoint)
    topPosts=response.json()
    for post in topPosts:
        print(post)
        print("")

def searchComments():
    endpoint='http://127.0.0.1:8000/backend_test/search_posts/'
    body={
        "postId": 1,
        # "id": 1,
        # "name": "id labore ex et quam laborum",
        # "email": "Eliseo@gardner.biz",
        # "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
    }
    response=requests.post(endpoint, json=body)
    searchedComments=response.json()
    for comment in searchedComments:
        print(comment)
        print("")

searchComments()