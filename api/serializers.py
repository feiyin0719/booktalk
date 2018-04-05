from rest_framework import serializers

from authuser.models import Test1, Test2, Test3, MyUser
from book.models import Article


class Test1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Test1
        fields = '__all__'
class Test2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Test2
        fields = '__all__'
class Test3Serializer(serializers.HyperlinkedModelSerializer):
    # test2_link=serializers.HyperlinkedRelatedField(Test2.objects.all(),view_name='test2')
    class Meta:
        model = Test3
        fields = ['name','test2','url']
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=MyUser
        fields=['nickname','username','url','id']
class BookreadSerializer(serializers.HyperlinkedModelSerializer):
    createdate=serializers.DateTimeField(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name='bookread-detail')
    # owner=serializers.HyperlinkedRelatedField(read_only=True, default=serializers.CurrentUserDefault(),view_name='myuser-detail')
    owner=UserSerializer(read_only=True,default=serializers.CurrentUserDefault())
    type=serializers.IntegerField(read_only=True,default=0)
    class Meta:
        model=Article
        fields = ['title','content','url','cover','createdate','owner','type','id']
class BookshareSerializer(serializers.HyperlinkedModelSerializer):
    createdate=serializers.DateTimeField(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name='bookshare-detail')
    owner = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
    type = serializers.IntegerField(read_only=True,default=1)
    class Meta:
        model=Article
        fields = ['title','content','url','cover','createdate','owner','type','id']

