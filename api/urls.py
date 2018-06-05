from django.conf.urls import url,include

from api.views import course,deep_technology


urlpatterns = [
<<<<<<< HEAD
    # 方式四方式四
=======
<<<<<<< HEAD
    # 方式六
=======
    # fangshi5
>>>>>>> 1abfc16355583d0a9215c8074da9e4308d78a273
>>>>>>> bfaa3883e224d473fa52cb4f7803de3eee76e843
    # url(r'^course/$', course.CourseView.as_view()),
    # print(‘春生213’)
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
