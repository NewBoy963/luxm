from api.models import *
from rest_framework import serializers

# 文章
class Articleserializer(serializers.ModelSerializer):
    source = serializers.CharField(source='source.name')
    article_type = serializers.CharField(source='get_article_type_display')
    status = serializers.CharField(source='get_status_display')
    position = serializers.CharField(source='get_position_display')
    class Meta:
        model = Article
        fields = ['id','title','source','article_type','brief','head_img',
                  'content','pub_date','offline_date','status','order','vid',
                  'comment_num','agree_num','view_num','collect_num','date',
                  'position'
                  ]

# 收藏
class Collectionserializer(serializers.ModelSerializer):
    content_type=serializers.CharField(source="content_type.model")
    content_object=serializers.CharField(source="content_object.title")
    account=serializers.CharField(source="account.username")
    class Meta:
        model = Collection
        fields = ['id', 'date', 'content_type','content_object','account']


# 评论
class Commentserializer(serializers.ModelSerializer):

    content_type = serializers.CharField(source='content_type.model')
    content_object=serializers.CharField(source="content_object.title")

    class Meta:
        model = Comment
        fields = ['content_type','content_object',]

