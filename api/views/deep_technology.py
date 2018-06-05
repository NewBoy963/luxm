from api.models import *
from api.serialize.deep_technology_serialize import *
from rest_framework.viewsets import GenericViewSet,ViewSetMixin
from rest_framework.views import APIView
from rest_framework.response import Response

class ArticleView(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            queryset = Article.objects.all()
            print(queryset,"1234564564")
            ser = Articleserializer(instance=queryset, many=True)
            print(ser, "1234564564")
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取文章失败'

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        """
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}

        try:
            # 课程ID=2
            pk = kwargs.get('pk')

            # 课程详细对象
            obj = models.CourseDetail.objects.filter(course_id=pk).first()

            ser = CourseDetailSerializer(instance=obj, many=False)

            ret['data'] = ser.data

        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)



class CollectionView(ViewSetMixin,APIView):

    ret = {'code': 1000, 'data': None}
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            queryset = Collection.objects.all()
            print(queryset, "11111111111")
            ser = Collectionserializer(instance=queryset, many=True)
            print(ser, "2222")
            ret['data'] = ser.data
        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取收藏失败'

        return Response(ret)

    # def retrieve(self, request, *args, **kwargs):
    #     """
    #     课程详细接口
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     ret = {'code': 1000, 'data': None}
    #
    #     try:
    #         # 课程ID=2
    #         pk = kwargs.get('pk')
    #
    #         obj = Collection.objects.filter(username_id=pk).first()
    #
    #         ser = Collectionserializer(instance=obj, many=False)
    #
    #         ret['data'] = ser.data
    #
    #     except Exception as e:
    #         ret['code'] = 1001
    #         ret['error'] = '获取课程失败'
    #
    #     return Response(ret)



class CommentView(ViewSetMixin,APIView):


    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            queryset = Comment.objects.all()
            print(queryset, "11111111111")
            ser = Commentserializer(instance=queryset, many=True)
            print(ser, "2222")
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取收藏失败2'

        return Response(ret)
