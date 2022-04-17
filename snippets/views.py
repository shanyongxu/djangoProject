from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from snippets.serializers import SnippetSerializer
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly

class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # 这里继承了三个类，Generics相当于基于类视图的APIVIEW类，这个基础类提供核心功能
    # 另外另个混合类提供list和create操作 大概的对应关系是get->list,post->create;请求的方法->具体的动作
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# retrieve是取回的意思，我一开始以为是select或者get， 但是发现不是这样的，get是请求的方法，不是动作
class SnippetDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# 其实写到这里，也应该可以感受的到，大部分代码都是重复的，但是我觉得这样写还不算特别的抽象，如果再次封装，更加抽象，后面维护起来就比较困难了

# 整体的思路大概就是一个具体的请求方法对应一个具体的动作

# 更加抽象的方法是使用混合好的通用视图，看到谁用这种混合好的通用视图，上去就是一个大逼斗

from snippets.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
