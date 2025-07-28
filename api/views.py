from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.models import Post
from post.serializer import PostSerializer
from rest_framework.views import APIView
from rest_framework import status


# @api_view(['GET'])
# def api_index(request):
#     result = {
#         "foo": "bar"
#     }
#     return Response(result)


# @api_view(['GET'])
# def get_all_posts(request):
#     posts = Post.objects.all().select_related('category')
#     serializer = PostSerializer(posts, many=True)

#     return Response(serializer.data)


class ListPosts(APIView):
    def get(self, request):
        posts = Post.objects.all().select_related("category")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):  
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    
class PostDetails(APIView):
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        serializer = PostSerializer(data = post.data)

        if serializer:
            return Response({
                "success" : True,
                "data" : serializer.data
            })
        return Response({
                "success" : False,
                "data" : serializer.errors
        })