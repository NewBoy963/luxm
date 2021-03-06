from django.conf.urls import url,include

from api.views import course,deep_technology


urlpatterns = [
    # 方
    # url(r'^course/$', course.CourseView.as_view()),
    # print(‘春生213’)
    # print('春生465')
    # print "987"
    # print('2B')  print('春生465')
    # url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view()),

    # 方式二
    url(r'^course/$', course.CourseView.as_view({'get':'list'})),
    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get':'retrieve'})),
    url(r'^article/$', deep_technology.ArticleView.as_view({'get':'list'})),
    url(r'^article/(?P<pk>\d+)/$', deep_technology.ArticleView.as_view({'get':'retrieve'})),
    url(r'^collection/$', deep_technology.CollectionView.as_view({'get': 'list'})),
    url(r'^collection/(?P<pk>\d+)/$', deep_technology.CollectionView.as_view({'get': 'retrieve'})),
    url(r'^comment/$', deep_technology.CommentView.as_view({'get': 'list'})),
    url(r'^comment/(?P<pk>\d+)/$', deep_technology.CommentView.as_view({'get': 'retrieve'}))
]
