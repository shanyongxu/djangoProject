from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # 说明一下，这里直接使用request.data,是因为我们使用api_view将此方法装饰之后，
        # request就会将原来的HttpRequest对象进行进一步封装，我们直接使用request.data
        # 就可以将post，put，patch方法的数据全部取出
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 这里使用REST扩展之后的Response作为返回的方法，将单纯的状态数字变成明确的标示符
            # 这就会使得相应意义更加明显
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 一般针对某个具体实例，有三种方法
@api_view(['get', 'put', 'delete'])
def snippet_detail(request, pk, format=None):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = request.data
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
